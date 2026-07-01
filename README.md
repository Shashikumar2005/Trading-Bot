# Binance Futures Trading Bot (Testnet)

A Python-based command-line trading bot that places MARKET and LIMIT orders on the Binance USDT-M Futures Testnet (Demo Trading).

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command-line interface using argparse
- Input validation
- Structured project architecture
- Logging of requests, responses, and errors
- Exception handling

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

## Usage

### MARKET BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### MARKET SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### LIMIT BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 90000
```

### LIMIT SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading.log
```

## Error Handling

The application handles:

- Invalid symbol
- Invalid quantity
- Invalid price
- Invalid order type
- API errors
- Network failures

## Assumptions

- Binance Demo Trading account is configured.
- API key has Futures permissions.
- Orders are placed on the Binance Futures Testnet/Demo environment.