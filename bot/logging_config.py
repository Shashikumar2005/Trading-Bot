"""
Logging configuration.
Creates logs/trading.log automatically.
"""

import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "trading.log")

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TradingBot")