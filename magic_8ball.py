"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Without a doubt",
    "Very unlikely",
    "The signs point to yes",
    "Cannot predict now"
)

print("Welcome to the Digital Oracle!")

while True:
    question = input("Ask a question (or type quit): ").strip().lower()

    if "quit" in question:
        print("Goodbye.")
        break

    print(random.choice(RESPONSES))