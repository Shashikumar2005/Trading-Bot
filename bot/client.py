"""
Binance Futures REST Client
"""

import hashlib
import hmac
import time
import urllib.parse

import requests

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import logger


class BinanceClient:
    """Simple Binance Futures REST Client."""

    def __init__(self):
        self.base_url = BASE_URL

        self.headers = {
            "X-MBX-APIKEY": API_KEY
        }

    # -------------------------------------------------
    # Generate Signature
    # -------------------------------------------------

    def _generate_signature(self, params):

        query = urllib.parse.urlencode(params)

        return hmac.new(
            API_SECRET.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()

    # -------------------------------------------------
    # Send Signed Request
    # -------------------------------------------------

    def _send_request(self, method, endpoint, params=None):

        if params is None:
            params = {}

        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000

        params["signature"] = self._generate_signature(params)

        url = self.base_url + endpoint

        logger.info(f"{method} {url}")
        logger.info(params)

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            timeout=30,
        )

        logger.info(response.text)

        try:
            data = response.json()
        except Exception:
            response.raise_for_status()

        if response.status_code >= 400:

            message = data.get("msg", "Unknown Error")
            code = data.get("code", response.status_code)

            if code == -4164:
                raise Exception(
                    "Order value must be at least 50 USDT. Increase the quantity."
                )

            if code == -2019:
                raise Exception(
                    "Margin is insufficient. Check your Demo Futures account."
                )

            raise Exception(
                f"Binance Error {code}: {message}"
            )

        return data

    # -------------------------------------------------
    # Ping
    # -------------------------------------------------

    def ping(self):

        return requests.get(
            self.base_url + "/fapi/v1/ping"
        ).json()

    # -------------------------------------------------
    # Server Time
    # -------------------------------------------------

    def server_time(self):

        return requests.get(
            self.base_url + "/fapi/v1/time"
        ).json()

    # -------------------------------------------------
    # Market Order
    # -------------------------------------------------

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
    ):

        params = {

            "symbol": symbol,

            "side": side,

            "type": "MARKET",

            "quantity": quantity,

        }

        return self._send_request(
            "POST",
            "/fapi/v1/order",
            params,
        )

    # -------------------------------------------------
    # Limit Order
    # -------------------------------------------------

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
    ):

        params = {

            "symbol": symbol,

            "side": side,

            "type": "LIMIT",

            "quantity": quantity,

            "price": price,

            "timeInForce": "GTC",

        }

        return self._send_request(
            "POST",
            "/fapi/v1/order",
            params,
        )