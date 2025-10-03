## MATH FUNCTIONS
def add_nums(num1, num2):
    return num1 + num2


def subtract_nums(num1, num2):
    return num1 - num2


def multiply_nums(num1, num2):
    return num1 * num2


def divide_nums(num1, num2):
    try:
        num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
        return

    return num1 / num2


## VALIDATE INPUT
def check_input(input_array):
    math_operators = "+-*/"

    if len(input_array) != 3:
        return False

    try:
        int(input_array[0])
        int(input_array[2])
    except ValueError:
        return False

    if input_array[1] not in math_operators:
        return False

    return True


## MAIN LOOP
while True:
    ## DECLARE ARRAY AND CLEAR EVERY ITERATION
    user_input = []

    print("=== Joes Calculator ===")
    print("Math Operators: +  -  *  /")
    user_input = input("Enter problem(example: 3 * 3) or type exit to quit: ").split()
    print("")

    ## CHECK FOR NO INPUT
    if len(user_input) == 0:
        print("")
        print("No input given.")
        print("")
        continue

    ## CHECK FOR EXIT
    if user_input[0] == "exit":
        print("Quitting program")
        exit()

    ## CHECK IF USER INPUT IS VALID
    if not check_input(user_input):
        print("")
        print("Invalid number or operator. Check syntax.")
        print("")
        continue

    ## DECLARE VARS AFTER VALIDATION
    num1 = int(user_input[0])
    num2 = int(user_input[2])
    operator = user_input[1]

    ## CHECK OPERATOR AND SEND TO PROPER FUNCTION
    if operator == "+":
        print(f" {num1} {operator} {num2} = {add_nums(num1, num2)}")

    if operator == "-":
        print(f" {num1} {operator} {num2} = {subtract_nums(num1, num2)}")

    if operator == "*":
        print(f" {num1} {operator} {num2} = {multiply_nums(num1, num2)}")

    if operator == "/":
        print(f" {num1} {operator} {num2} = {divide_nums(num1, num2)}")

    print("")
