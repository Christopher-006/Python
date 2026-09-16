"""
Thinking CRUD

🏗️  Create
📖  Read
🔃  Update
🗑️  Delete

💡When we get to crud, we will present users with a menu of choices. This is a standard interface module. Now that we know Match Case, it makes menu choices easy. It will get even easier when we get to functions.
"""

# Match case for menu
# Display menu
print(f" 1.  Create a new contact")
print(f" 2.  Search contacts")
print(f" 3.  Update contact")
print(f" 4.  Delete a contact")
print(f" 5.  Quit")

# get user choice
choice = 1
while choice > 0 and choice < 4:
    choice = int(input("Please enter the number of your selection:  "))
    match choice:

        case 1:
            print("Create")
        case 2:
            print("Search")  # read
        case 3:
            print("Update")
        case 4:
            print("Delete")
        case 5:
            print("Good bye!")
