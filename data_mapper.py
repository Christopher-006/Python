"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

NATO_ALPHABET = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

while True:
    print("\n1. Enter English")
    print("2. Enter coded word")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        word = input("Enter word to spell: ").upper()

        for letter in word:
            try:
                print(NATO_ALPHABET[letter], end=" ")
            except KeyError:
                print("?", end=" ")

        print()

    elif choice == "2":
        coded_word = input("Enter coded word: ").title()

        reverse_nato = {}

        for key, value in NATO_ALPHABET.items():
            reverse_nato[value] = key

        words = coded_word.split()

        for word in words:
            try:
                print(reverse_nato[word], end="")
            except KeyError:
                print("?", end="")

        print()

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")