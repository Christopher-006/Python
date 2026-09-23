"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
---------------
balance = 1000.00

print(" 1. View Balance")
print(" 2. Deposit")
print(" 3. Withdraw")
print(" 4. Transfer")
print(" 5. Quit")

choice = 1

while 1 <= choice <= 5:
    choice = int(input("Please enter the number of your selection: "))

    match choice:
        case 1:
            print(f"Your current balance is: ${balance:.2f}")

        case 2:
            deposit_amount = float(input("Enter deposit amount: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Deposit successful! New balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount.")

        case 3:
            withdraw_amount = float(input("Enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Overdraft! You don't have enough money.")
            elif withdraw_amount <= 0:
                print("Invalid withdraw amount.")
            else:
                balance -= withdraw_amount
                print(f"Withdraw successful! New balance: ${balance:.2f}")

        case 4:
            transfer_amount = float(input("Enter transfer amount: "))
            if transfer_amount > balance:
                print("Overdraft! You don't have enough money.")
            elif transfer_amount <= 0:
                print("Invalid transfer amount.")
            else:
                balance -= transfer_amount
                print(f"Transfer successful! New balance: ${balance:.2f}")

        case 5:
            print("Goodbye!")
            break

        case _:
            print("Invalid Selection")
