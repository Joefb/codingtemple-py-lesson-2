# 1. create fun takes in array
#     - iterate array and add nums store in sum var
#     - divide array len by sum to get average
#     - return average
#
# 2. create fun takes in int
#    - if int >90 return A
#    - if int 80-89 return B
#    - if int 70-79 return C
#    - if int 60-69 return D
#    - if int <60 return F
#
# 3. main code
#   - ask how many scores store in var
#   - ask for scores store in array, use for loop
#   - for score in range(num_of_scores + 1) arr.append()


## CALC AVERAGE
def calculate_average(nums_array):
    nums_sum = 0

    for nums in nums_array:
        nums_sum += nums

    return nums_sum / len(nums_array)


### GET GRADE
def get_letter_grade(average):
    grade = None

    if average >= 90:
        grade = "A"

    if average >= 80 and average <= 89:
        grade = "B"

    if average >= 70 and average <= 79:
        grade = "C"

    if average >= 60 and average <= 69:
        grade = "D"

    if average < 60:
        grade = "F"

    return grade


## PRINT INTRO
print("")
print("### Grade Average Calculator ###")
print("")

## GET AMOUNT OF SCORES AND DECLARE ARRAY
# num_of_scores = int(input("Enter the number of scores you need to enter: "))
scores_array = []

## GET SCORES
# for num in range(1, num_of_scores + 1):
#     scores_array.append(int(input(f"Enter score {num}: ")))

## REFACTOR CODE FOR FUN
## GET SCORES UNTIL DONE IS ENTERED
done_getting_scores = False

while not done_getting_scores:
    # RESET SCORE EVERY ITERATION
    score = None
    print(f"Current scores: {scores_array}")
    print("Enter score. Type done when done entering scores.")
    score = input("Score: ").lower()

    if score == "done":
        done_getting_scores = True

    ## CHECK IF INPUT WAS ENTERED, IF NOT SHOW ERROR
    elif len(score) == 0:
        print("")
        print("No score entered. Enter score or type done when done entering scores.")
        print("")

    else:
        ## CHECK IF INT, IF NOT PRINT ERROR.
        try:
            score = int(score)

            if score > 100 or score < 0:
                print("")
                print("Invalid number. Cannot have a score above 100 or below 0.")
                print("")
                continue

            scores_array.append(score)
        except ValueError:
            print(
                "Invalid number. Enter valid number or type done when done entering scores."
            )
            print("")

## CHECK TO SEE IF USER ENTERED DONE ON THE FIRST ITERATION
if len(scores_array) == 0:
    print("No scores entered. Exiting program")
    exit()

## GET AVERAGE AND LETTER GRADE
average = calculate_average(scores_array)
grade = get_letter_grade(average)

## GRADE REPORT
print("")
print("### GRADE REPORT ###")
print(f"Test Scores: {scores_array}")
print(f"Average Score: {average:.1f}")
print(f"Letter Grade: {grade}")
