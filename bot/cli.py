"""
CLI Entry Point for Binance Futures Trading Bot
"""

import argparse
import sys

from bot.orders import OrderManager


def main():
    """
    Main CLI function.
    """

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side",
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type",
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity",
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT orders)",
    )

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        parser.error("--price is required for LIMIT orders.")

    manager = OrderManager()

    try:

        print("\n" + "=" * 50)
        print("ORDER REQUEST")
        print("=" * 50)

        print(f"Symbol     : {args.symbol}")
        print(f"Side       : {args.side}")
        print(f"Type       : {args.type}")
        print(f"Quantity   : {args.quantity}")

        if args.type == "LIMIT":
            print(f"Price      : {args.price}")

        print("=" * 50)

        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print("\n" + "=" * 50)
        print("ORDER RESPONSE")
        print("=" * 50)

        print(f"Order ID        : {response.get('orderId')}")
        print(f"Status          : {response.get('status')}")
        print(f"Symbol          : {response.get('symbol')}")
        print(f"Side            : {response.get('side')}")
        print(f"Executed Qty    : {response.get('executedQty')}")
        print(f"Average Price   : {response.get('avgPrice', 'N/A')}")

        print("\n Order placed successfully.")

    except Exception as e:

        print("\n Failed to place order.")
        print(f"Reason: {e}")

        sys.exit(1)


if __name__ == "__main__":
    main()