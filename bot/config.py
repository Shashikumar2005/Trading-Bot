"""
Configuration File
"""

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

if not API_KEY:
    raise ValueError("Missing API Key")

if not API_SECRET:
    raise ValueError("Missing API Secret")