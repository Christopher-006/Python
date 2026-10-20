"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Taco Stand Ordering System
"""

MENU_ITEMS = (
    "Tacos Al Pastor",
    "Tacos de Lengua",
    "Tacos de Asada",
    "Torta",
    "Tostadas"
)


def login():
    """Gets customer information."""
    pass


def past_orders(customer):
    """Checks for previous orders."""
    pass


def take_order(customer):
    """Collects taco order information."""
    pass


def verify_order(order):
    """Displays order for confirmation."""
    pass


def save_order(order):
    """Saves order information."""
    pass


def display_order(order):
    """Displays customer receipt."""
    pass


def main():
    customer = login()
    saved = past_orders(customer)
    order = take_order(customer)
    verify_order(order)
    save_order(order)
    display_order(order)


main()