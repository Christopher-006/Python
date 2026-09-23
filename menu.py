


# initialize 1000.00
balance = 1000.00
print(f" 1.  View Balance")
print(f" 2.  Deposit")
print(f" 3.  Withdraw")
print(f" 4.  Transfer")
print(f" 5.  Quit")

# get user choice
choice = 1
while choice > 0 and choice < 6:
    choice = int(input("Please enter the number of your selection:  "))
    match choice:

        case 1:
            print(f"Your current balance is: {balance}")
            continue
        case 2:
            deposit_amount = float(input("Enter deposit amount: "))
            print(f"Get deposit amt -> Validate it is numeric -> Add to balance: {deposit_amount}")
            continue
        case 3:
            withdraw_amount = float(input("Enter withdraw amount: "))
            print(f"Get withdraw amt -> Validate it is numeric -> Check for Overdraft -> Subtract: {withdraw_amount}")
            continue
        case 4:
            transfer_amount = float(input("Enter transfer amount: "))
            print(f"Get transfer amt -> Validate it is numeric -> Check for Overdraft -> Subtract: {transfer_amount}")
            continue
        case 5:
            print(f"Print goodbye -> Break loop")
            break
        case _:
            print(f"Invalid Selection")
