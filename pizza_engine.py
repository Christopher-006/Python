"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("Pepperoni", "Ham", "Pineapple", "Bacon")


def make_pizza(customer, size, topping, is_delivery=False):
    """
    :param customer:
    :param size:
    :param topping:
    :param is_delivery:
    """
    print("\n--- PIZZA ORDER ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery: {is_delivery}")


def main():
    customer = input("Customer Name: ").title().strip()

    print(f"Options: {TOPPINGS}")
    topping = input("Select Topping: ").title().strip()

    size = input("Pizza Size (Small, Medium, Large): ").title().strip()

    try:
        delivery = input("Delivery? (yes/no): ").lower().strip()
    except ValueError:
        delivery = "no"

    if delivery == "yes":
        delivery = True
    else:
        delivery = False

    make_pizza(
        customer=customer,
        size=size,
        topping=topping,
        is_delivery=delivery
    )


main()