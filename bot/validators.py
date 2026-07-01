"""
Input validation functions for the Trading Bot.
"""

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    """
    Validate trading symbol.
    """
    symbol = symbol.upper().strip()

    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    if len(symbol) < 6:
        raise ValueError("Invalid trading symbol.")
    if not symbol.endswith("USDT"):
        raise ValueError(
            "Only USDT Future symbolsare supported."
        )

    return symbol


def validate_side(side):
    """
    Validate order side.
    """
    side = side.upper().strip()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side '{side}'. Allowed values: BUY or SELL."
        )

    return side


def validate_order_type(order_type):
    """
    Validate order type.
    """
    order_type = order_type.upper().strip()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type '{order_type}'. Allowed values: MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity):
    """
    Validate order quantity.
    """
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price):
    """
    Validate limit order price.
    """
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    return price