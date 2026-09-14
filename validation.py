"""
 Error checking data entry with while statements
"""

# Name check


# Rules -can't be empty
# less than 30 characters
# should have the first letter capitalized
while not fname: 
    fname = input("Please enter your first name: ")
    fname = fname.strip()


age = -1
while age < 0:
    age = input("Please enter your age: ")
    if not age.isdigit():
        print("Error: Age must be a positive number.")
        age = -1
    else:
        age = int(input("Please enter your child's age: (whole years, round down) "))
    except ValueError:
        print("I'm sorry, but that is not a valid age.")
    except Exception as e:
    print(f"Error: {e}")