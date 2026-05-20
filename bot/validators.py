def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be a positive number greater than zero.")
    return quantity

def validate_price(order_type: str, price: float = None) -> float:
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("A valid positive price is required for LIMIT orders.")
        return price
    return None