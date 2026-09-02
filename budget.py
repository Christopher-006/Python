 #  get info from user

gross_income = float((input"What is your gross monthly income? "))
housing = float((input"What do you spend on your rent or mortgage"))
phone = float((input"What do you spend on your phone each month"))

net_income = gross_income * .8


total_expenses = phone + housing
remaining = net_income - total_expenses

print(f"You spent a total of {total_expenses:,.2f}")
""
               " $"
