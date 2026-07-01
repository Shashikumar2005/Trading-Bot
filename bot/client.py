"""
Binance Futures Client Wrapper

Handles:
- Connection to Binance Futures Testnet
- Market Orders
- Limit Orders
- API Error Handling
"""

from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import logger


class BinanceClient:
    """
    Wrapper class for Binance Futures Testnet.
    """

    def __init__(self):
        try:
            self.client = Client(API_KEY, API_SECRET)

            # Use Binance Futures Testnet
            self.client.FUTURES_URL = BASE_URL

            logger.info("Successfully connected to Binance Futures Testnet.")

        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise

    def place_market_order(self, symbol, side, quantity):
        """
        Place a MARKET order.
        """

        try:
            logger.info(
                f"Market Order Request | "
                f"Symbol={symbol}, Side={side}, Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info(f"Market Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        """
        Place a LIMIT order.
        """

        try:
            logger.info(
                f"Limit Order Request | "
                f"Symbol={symbol}, Side={side}, Qty={quantity}, Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(f"Limit Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise

    def get_server_time(self):
        """
        Check API connectivity.
        """

        return self.client.futures_time()