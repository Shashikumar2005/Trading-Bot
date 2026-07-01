"""
Order processing logic.

This module validates user input and places the requested order
using the Binance client.
"""

from bot.client import BinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import logger


class OrderManager:
    """
    Handles order validation and order placement.
    """

    def __init__(self):
        self.client = BinanceClient()

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
    ):
        """
        Validate inputs and place an order.

        Parameters:
            symbol (str)
            side (BUY/SELL)
            order_type (MARKET/LIMIT)
            quantity (float)
            price (float, optional)

        Returns:
            dict : Binance API response
        """

        try:

            # -------------------------
            # Validate Inputs
            # -------------------------

            symbol = validate_symbol(symbol)
            side = validate_side(side)
            order_type = validate_order_type(order_type)
            quantity = validate_quantity(quantity)

            # -------------------------
            # MARKET ORDER
            # -------------------------

            if order_type == "MARKET":

                logger.info("Processing MARKET order.")

                return self.client.place_market_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity,
                )

            # -------------------------
            # LIMIT ORDER
            # -------------------------

            if price is None:
                raise ValueError(
                    "Price is required for LIMIT orders."
                )

            price = validate_price(price)

            logger.info("Processing LIMIT order.")

            return self.client.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        except Exception as e:

            logger.error(f"Order processing failed: {e}")

            raise