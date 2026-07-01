"""
Binance Futures Client Wrapper
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
            self.client = Client(
                api_key=API_KEY,
                api_secret=API_SECRET,
            )

            # Point Futures API to Testnet
            self.client.FUTURES_URL = BASE_URL

            logger.info("Connected to Binance Futures Testnet.")

        except Exception:
            logger.exception("Failed to initialize Binance client.")
            raise

    def get_server_time(self):
        """Check API connectivity."""
        return self.client.futures_time()

    def place_market_order(self, symbol, side, quantity):
        try:

            logger.info(
                f"Submitting MARKET order | "
                f"Symbol={symbol}, Side={side}, Quantity={quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info(f"Response: {response}")

            return response

        except BinanceAPIException:
            logger.exception("Binance API Error")
            raise

        except Exception:
            logger.exception("Unexpected Error")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:

            logger.info(
                f"Submitting LIMIT order | "
                f"Symbol={symbol}, Side={side}, "
                f"Quantity={quantity}, Price={price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(f"Response: {response}")

            return response

        except BinanceAPIException:
            logger.exception("Binance API Error")
            raise

        except Exception:
            logger.exception("Unexpected Error")
            raise