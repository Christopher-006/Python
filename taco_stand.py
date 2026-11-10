
"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""
MENU_ITEMS = (
    "Tacos Al Pastor",
    "Tacos de Lengua",
    "Tacos de Asada",
    "Torta",
    "Tostadas"
)



import datetime


def save_order(order, customer):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("order_history.txt", "a") as file:
        file.write(f"{current_time},{customer},{order}\n")

    with open("receipts.txt", "a") as file:
        file.write(f"""
--------------------------------
TACO STAND RECEIPT
Customer: {customer}
Order: {order}
Date: {current_time}
--------------------------------

""")


def view_orders():
    try:
        with open("order_history.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No previous orders found.")


def main():
    customer = input("Customer Name: ")

    while True:
        choice = input("Enter order, review, or quit: ").lower()

        if choice == "quit":
            break

        if choice == "review":
            view_orders()

        if choice == "order":
            item = input("Enter menu item: ")
            save_order(item, customer)


main()
