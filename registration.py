"""
ASSIGNMENT 5A: INPUT VALIDATION
Requirements:
- First Name & Last Name: Cannot be blank.
- Age: Must be a number; check if 21+ for drink ticket.
- Phone Number: Cannot be blank.
- Ticket Count: Must be a valid integer > 0.
- Additional Tickets? (Y/N)
"""

try:

    first_name = input("Enter First Name: ").strip()
    while first_name == "":
        print("Error: First name cannot be blank.")
        first_name = input("Enter First Name: ").strip()

    last_name = input("Enter Last Name: ").strip()
    while last_name == "":
        print("Error: Last name cannot be blank.")
        last_name = input("Enter Last Name: ").strip()

    age_ok = False
    while age_ok == False:
        try:
            age = int(input("Enter Age: ").strip())
            age_ok = True
        except ValueError:
            print("Error: Age must be a number.")

    if age >= 21:
        drink_ticket = "Yes"
    else:
        drink_ticket = "No"

    phone = input("Enter Phone Number: ").strip()
    while phone == "":
        print("Error: Phone number cannot be blank.")
        phone = input("Enter Phone Number: ").strip()

    ticket_ok = False
    while ticket_ok == False:
        try:
            tickets = int(input("How many tickets? ").strip())
            if tickets > 0:
                ticket_ok = True
            else:
                print("Error: Must be at least 1 ticket.")
        except ValueError:
            print("Error: Please enter a number for tickets.")

    more = input("Would you like additional tickets? (Y/N): ").strip().upper()
    while more != "Y" and more != "N":
        print("Error: Please enter Y or N.")
        more = input("Would you like additional tickets? (Y/N): ").strip().upper()

    print("\nRegistration Complete!")
    print("Name:", first_name, last_name)
    print("Age:", age, "| Drink Ticket:", drink_ticket)
    print("Phone:", phone)
    print("Tickets Ordered:", tickets)
    print("Additional Tickets:", more)

except ValueError:
    print("A value error happened. Please restart the program.")

except Exception as e:
    print("Unexpected error:", e)
