"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""


"""
# --- The People ---
host = "Maya"
judge = "Liam"
contest = "The Midnight Math-Off"

print(f"{host} and {judge} are hosting {contest}.")
print(f"Tonight, two contestants submit scores and the judges use a tiny calculator to decide the outcome.")
print("-" * 60)


num1 = int(input("Enter the first integer (num1) — contestant A's score: "))
num2 = int(input("Enter the second integer (num2) — contestant B's score: "))


both_positive = (num1 > 0 and num2 > 0)            # Both > 0
both_over_100 = (num1 > 100 and num2 > 100)       # Both > 100
either_even = (num1 % 2 == 0 or num2 % 2 == 0)    # Either Even (uses modulus)
either_under_100 = (num1 < 100 or num2 < 100)     # Either < 100
not_equal = (num1 != num2)                        # Not Equal
neither_zero = (num1 != 0 and num2 != 0)          # Not Zero


print("\n--- Scoreboard (logical checks) ---")
print(f"{host}: 'Both scores positive? {both_positive}'")
print(f"{judge}: 'Both over 100? {both_over_100}'")
print(f"{host}: 'At least one even? {either_even}'")
print(f"{judge}: 'At least one under 100? {either_under_100}'")
print(f"{host}: 'Are the scores different? {not_equal}'")
print(f"{judge}: 'Neither score is zero? {neither_zero}'")

if num1 > 0:
    num1_category = "Positive"
elif num1 < 0:
    num1_category = "Negative"
else:
    num1_category = "Zero"

print(f"\nnum1 category: {num1_category}")


print("\n--- Final announcement from the stage ---")
if both_over_100 and neither_zero:
    print(f"{host}: 'Both contestants crushed it — every judge is impressed. A standing ovation!'")
elif both_positive and either_even:
    print(f"{judge}: 'Both scores are positive and at least one is even — solid performances all around.'")
elif not_equal and either_under_100:
    print(f"{host}: 'The scores differ and at least one is under 100 — a close call, but the crowd loved the drama.'")
elif not neither_zero:
    print(f"{judge}: 'One of the scores is zero — someone got distracted. We'll give them another chance.'")
else:
    print(f"{host}: 'Interesting results. {contest} will return next week with new challenges.'")

print("\nThanks for judging tonight's contest. See you at the next round!")
#comment

