"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Pineapple", "Raspberry", "Peach", "Cherry")


def get_price(size):
    match size:
        case "small":
            return 3.0
        case "medium":
            return 4.0
        case "large":
            return 5.0
        case _:
            print("Invalid entry")
            return 0.0


def blend(size, base, fruit, scoops):
    print("\n--- Smoothie Order ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")


def main():
    size = input(
        "What size smoothie do you want (small, medium, large): "
    ).lower().strip()

    print(BASES)
    base = input("Choose a base: ")

    print(FRUITS)
    fruit = input("Choose a fruit: ")

    try:
        scoops = int(input("How many scoops would you like? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1 scoop.")
        scoops = 1

    price = get_price(size)

    blend(size, base, fruit, scoops)

    print(f"Total Bill: ${price:.2f}")


main()