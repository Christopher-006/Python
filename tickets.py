"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
This program manages a list of available theater seats and removes them
as customers purchase tickets.
-----------------------------------------------------------------------
"""

def main():
    available_seats = list(range(1, 21))

    print("Welcome to the Theater Ticket Kiosk!")
    print("Enter 0 at any time to quit.\n")

    while True:
        if len(available_seats) == 0:
            print("All seats have been sold! Enjoy the show!")
            break

        print(f"Available Seats: {available_seats}")

        user_input = input("Choose a seat number (0 to quit): ").strip()

        if not user_input.isdigit():
            print("Invalid input. Please enter a number.\n")
            continue

        choice = int(user_input)

        if choice == 0:
            print("Thanks for visiting!")
            break

        if choice not in range(1, 21):
            print("That seat number does not exist.\n")
            continue

        if choice not in available_seats:
            print("That seat is already taken.\n")
            continue

        available_seats.remove(choice)
        print(f"Seat {choice} reserved successfully!\n")

if __name__ == "__main__":
    main()
#comment