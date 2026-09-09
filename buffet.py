"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [9/2/2026]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)(make a variable, change to .5 if it is Tuesday)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price! (changes price calculation)
   - Sunday: Drinks are free! (print statement no change in price)
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""
# Ask for the day and normalize to lowercase
day_of_week = input("Please enter the day of the week: ").lower()
 # Set the child price per year using match/case
match day_of_week:
    case "tuesday":
        child_price_per_year = 0.50
    case "sunday":
        child_price_per_year = 1.00
        print("Drinks are free")
    case _:
        child_price_per_year = 1.00
       # Use age 16 as requested (no input)
age = 16
# Determine the price using one if/elif/else chain
if age < 1:
    price = 0.00
elif age <= 12:
    price = age * child_price_per_year
elif age <= 64:
    price = 16.95
else:
    price = 12.95

# Print the final price formatted as currency
print(f"Your total is ${price:.2f}")
#comment

