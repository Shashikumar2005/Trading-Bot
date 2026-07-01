"""
Binance Futures Client Wrapper

Responsible for:
- Connecting to Binance Futures Testnet
- Placing Market Orders
- Placing Limit Orders
- Logging API requests and responses
- Handling Binance API exceptions
"""

from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.config import API_KEY, API_SECRET
from bot.logging_config import logger


class BinanceClient:
    """
    Wrapper around python-binance for Binance Futures Testnet.
    """

    def __init__(self):
        try:
            # Connect to Binance Futures Testnet
            self.client = Client(
                api_key=API_KEY,
                api_secret=API_SECRET,
                testnet=True
            )

            logger.info("Connected to Binance Futures Testnet.")

        except Exception as e:
            logger.exception("Failed to initialize Binance client.")
            raise e

    def get_server_time(self):
        """
        Check API connection.
        """
        return self.client.futures_time()

    def place_market_order(self, symbol, side, quantity):
        """
        Place a MARKET order.
        """

        try:
            logger.info(
                f"Submitting MARKET order | "
                f"Symbol={symbol}, Side={side}, Qty={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Market Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.exception("Binance API Error")
            raise e

        except Exception as e:
            logger.exception("Unexpected Error")
            raise e

    def place_limit_order(self, symbol, side, quantity, price):
        """
        Place a LIMIT order.
        """

        try:
            logger.info(
                f"Submitting LIMIT order | "
                f"Symbol={symbol}, Side={side}, Qty={quantity}, Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Limit Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logger.exception("Binance API Error")
            raise e

        except Exception as e:
            logger.exception("Unexpected Error")
            raise e