# **Intro to Python \- Homework Assignment: Lessons 1-4**

## **Variables, Control Flow, Loops & Functions**

**Important Instructions:**

- **Create a Python file in VS Code** for each question (e.g., question1.py, question2.py, etc.)
- Test each program to make sure it works correctly
- Save all your Python files in a folder called "homework"
- For each question below, write the code in the appropriate Python file.
- Push the work up to a github repository, and submit the link to the repo

---

## **Question 1: Personal Budget**

Create a budget calculator using a function that tracks income and expenses.

**Requirements:**

- Create a function called calculate_budget() that:
  - Asks the user for their monthly income
  - Asks for 3 expenses: rent, food, and entertainment
  - Calculates total expenses and remaining money
  - Uses if/elif/else to give budget advice:
    - If remaining money \< 0: "You're overspending\! Cut back on expenses."
    - If remaining money \< 100: "Your budget is tight. Be careful with spending."
    - If remaining money \>= 100: "Great job\! You have money left over."
  - Displays a formatted summary
- Call the function at the end of your program

**Create file:** question1.py

**Example Output:**

```
Enter your monthly income: $3000
Enter rent expense: $1200
Enter food expense: $400
Enter entertainment expense: $300

=== BUDGET SUMMARY ===
Monthly Income: $3000.00
Total Expenses: $1900.00
Remaining Money: $1100.00

Budget Advice: Great job! You have money left over.
```

---

## **Question 2: Simple Calculator Functions (Lesson 4 \- Functions)**

Create a calculator using functions for different operations.

**Requirements:**

- Create these functions:
  - add(a, b) \- returns the sum of two numbers
  - subtract(a, b) \- returns the difference of two numbers
  - multiply(a, b) \- returns the product of two numbers
  - divide(a, b) \- returns the quotient, handles division by zero
- Create a main function that:
  - Gets two numbers from the user
  - Asks which operation to perform
  - Calls the appropriate function
  - Displays the result

**Create file:** question2.py

**Example Output:**

```
Enter first number: 15
Enter second number: 3
Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1-4): 4

15.0 ÷ 3.0 = 5.0

Enter first number: 10
Enter second number: 0
Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1-4): 4

Error: Cannot divide by zero!
```

---

## **Question 3: Grade Average Calculator (Lessons 1-4 Combined)**

Build a grade calculator that uses loops and functions to process student scores.

**Requirements:**

- Create a function calculate_average(scores) that:
  - Takes a list of scores as a parameter
  - Calculates and returns the average
- Create a function get_letter_grade(average) that:
  - Takes an average score as a parameter
  - Returns letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60\)
- Use a while loop to:
  - Ask how many test scores to enter
  - Collect each score from the user
  - Store scores in a list
- Display the average and letter grade using your functions

**Create file:** question3.py

**Example Output:**

```
How many test scores do you want to enter? 4
Enter score 1: 85
Enter score 2: 92
Enter score 3: 78
Enter score 4: 88

=== GRADE REPORT ===
Test Scores: [85, 92, 78, 88]
Average Score: 85.75
Letter Grade: B

Enter score 1: 95
Enter score 2: 87
Enter score 3: 91

=== GRADE REPORT ===
Test Scores: [95, 87, 91]
Average Score: 91.0
Letter Grade: A
```

---

## **Getting Ready for Monday: Create Your Codewars Account**

**Before Monday's class, please complete this important step:**

1. **Visit [codewars.com](https://www.codewars.com/)**
2. **Click "Sign Up" and create a free account**
3. **Choose Python as your primary language**
4. **Complete the initial setup challenges (basic Python problems)**
5. **Write down your username** \- you'll need it for class

**What is Codewars?**  
Codewars is a platform where you solve coding challenges called "kata" to improve your programming skills. We will be going over this with you on Monday and showing you how to use it to practice Python concepts.

**Why are we using it?**

- Practice real programming problems
- Build problem-solving skills
- Track your progress as you learn
- Join a community of learners
- Prepare for coding interviews

**Getting Started Tips:**

- Start with 8 kyu problems (easiest level)
- Read the problem carefully before coding
- Test your solution with the provided examples
- Don't worry if you get stuck \- we'll practice together in class\!

---

## **Getting Help**

If you get stuck:

1. Review the lesson materials from lessons 1-4
2. Start with simple versions and add features gradually
3. Test your code frequently as you write it
4. Use print statements to debug your logic
5. Ask questions during office hours or in class
6. Remember to save your work frequently in VS Code

**Remember:** This homework covers all the fundamentals\! Each question builds on what you've learned. Take your time, and focus on understanding the concepts rather than just getting the "right" answer.
