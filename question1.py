### BUDGET CALC FUNCTION
def calculate_budget(money_arr):
    money_spent = money_arr[1] + money_arr[2] + money_arr[3]
    money_leftover = money_arr[0] - money_spent

    return money_spent, money_leftover


### CREATE ARRAY TO HOLD 4 MONEY VALUES
budget_money = []


### CREATE ARRAY TO HOLD INCOME AND EXPENSES NAMES
income_expenses = ["income", "rent", "food", "entertainment"]


### COLLECT INCOME DATA
print("---- Budget Calculator ---- ")
try:
    for ele in income_expenses:
        budget_money.append(int(input(f"Please enter total amount for {ele}$ ")))

except ValueError:
    print("Invalid input. Please enter a number.")
    exit()


### CALCULATE BUDGET USING FUNCTION
money_spent, money_leftover = calculate_budget(budget_money)


### DISPLAY RESULTS
print("---- BUDGET SUMMARY -----")
print(f"Monthly Income: ${budget_money[0]}")
print(f"Total Expenses: ${money_spent}")
print(f"Remaining Money: ${money_leftover}")


# DISPLAY RESULTS
if money_leftover < 0:
    print(f"Your overspending by ${money_leftover * -1}! Cut back on the expenses!")
    exit()

if money_leftover < 100:
    print(
        f"Your budget is tight! You only have ${money_leftover} left. Be careful with your spending."
    )
    exit()

if money_leftover >= 100:
    print(f"Great job! You have ${money_leftover} left over!")
    exit()
