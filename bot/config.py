"""
Configuration settings for the Trading Bot.
Loads API credentials from the .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Binance Futures Testnet URL
BASE_URL = "https://testnet.binancefuture.com"

# Validate API credentials
if not API_KEY or not API_SECRET:
    raise ValueError(
        "API Key or Secret not found. Please check your .env file."
    )