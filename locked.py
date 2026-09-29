"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

DEPARTMENT_NAME = "INFORMATION TECHNOLOGY"

USER_NAMES = ("Alice", "Bob", "Charlie")
passwords = ["pass123", "qwerty", "letmein"]

print("Welcome to the Department Security Terminal.")
print(f"Department: {DEPARTMENT_NAME}")
print("----------------------------------------------")

running = True

while running:
    print("\nMenu Options:")
    print("1. Look up a username")
    print("2. Change a username (locked)")
    print("3. Change a password")
    print("4. Quit")

    try:
        choice = int(input("Enter your selection: "))
    except ValueError:
        print("Invalid input. Please enter a number from the menu.")
        continue

    if choice == 1:
        name = input("Enter the username to look up: ")
        if name in USER_NAMES:
            index = USER_NAMES.index(name)
            print(f"User found: {name}")
            print(f"Password: {passwords[index]}")
        else:
            print("User not found.")

    elif choice == 2:
        print("WARNING: Usernames are locked and cannot be changed.")
        try:
            index = int(input("Enter the index of the username to change: "))
            new_name = input("Enter the new username: ")
            USER_NAMES[index] = new_name
        except TypeError:
            print("ERROR: Usernames cannot be changed. Please email the help desk.")
        except (ValueError, IndexError):
            print("Invalid index. Please try again.")

    elif choice == 3:
        name = input("Enter the username whose password you want to change: ")
        if name in USER_NAMES:
            index = USER_NAMES.index(name)
            try:
                new_pass = input("Enter the new password: ")
                passwords[index] = new_pass
                print("Password updated successfully.")
            except Exception:
                print("Unexpected error. Please try again.")
        else:
            print("User not found.")

    elif choice == 4:
        print("Exiting terminal. Goodbye.")
        running = False

    else:
        print("Invalid selection. Please choose a valid menu option.")
