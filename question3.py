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
num_of_scores = int(input("Enter the number of scores you need to enter: "))
scores_array = []

## GET SCORES
for num in range(1, num_of_scores + 1):
    scores_array.append(int(input(f"Enter score {num}: ")))

## GET AVERAGE AND LETTER GRADE
average = calculate_average(scores_array)
grade = get_letter_grade(average)

## GRADE REPORT
print("### GRADE REPORT ###")
print(f"Test Scores: {scores_array}")
print(f"Average Score: {average}")
print(f"Letter Grade: {grade}")
