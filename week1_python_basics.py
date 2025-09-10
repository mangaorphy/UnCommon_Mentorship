"""
==============================================
WEEK 1: PYTHON BASICS - GETTING STARTED
==============================================
This file contains the fundamental Python concepts for Week 1 of the course.
Students will learn variables, data types, operators, and basic I/O.
"""

# ==============================================
# 1. WELCOME TO PYTHON!
# ==============================================

"""
Python is a powerful, easy-to-learn programming language.
It's used for:
- Web development (Django, Flask)
- Data science and AI
- Automation and scripting
- Desktop applications
- And much more!

This is a comment block. Comments help explain code.
"""

print("🐍 Welcome to Python Programming!")
print("=" * 40)

# ==============================================
# 2. VARIABLES - STORING INFORMATION
# ==============================================

"""
Variables are like labeled boxes where we store information.
Python variables don't need type declarations - Python figures it out!
"""

print("\n📦 VARIABLES EXAMPLES:")

# String variables (text)
student_name = "Alice Johnson"
course_name = "Python to Django REST Framework"
university = "UnCommon Mentorship Programme"

# Numeric variables
student_age = 22
course_duration_weeks = 16
grade_percentage = 87.5

# Boolean variables (True/False)
is_enrolled = True
has_programming_experience = False
is_excited = True

print(f"Student: {student_name}")
print(f"Age: {student_age}")
print(f"Course: {course_name}")
print(f"Duration: {course_duration_weeks} weeks")
print(f"Current Grade: {grade_percentage}%")
print(f"Enrolled: {is_enrolled}")
print(f"Excited about learning: {is_excited}")

# ==============================================
# 3. DATA TYPES - DIFFERENT KINDS OF DATA
# ==============================================

print("\n🏷️ DATA TYPES IN PYTHON:")

# String (str) - Text data
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
greeting = f"Hello, {full_name}!"  # f-string formatting (modern way)

print(f"String example: {greeting}")
print(f"Type of greeting: {type(greeting)}")

# Integer (int) - Whole numbers
current_year = 2025
birth_year = 2000
age = current_year - birth_year

print(f"Integer example: {age}")
print(f"Type of age: {type(age)}")

# Float - Decimal numbers
height_meters = 1.75
weight_kg = 70.5
bmi = weight_kg / (height_meters ** 2)

print(f"Float example: BMI = {bmi:.2f}")
print(f"Type of BMI: {type(bmi)}")

# Boolean - True or False
is_adult = age >= 18
is_teenager = 13 <= age <= 19

print(f"Boolean example: Is adult? {is_adult}")
print(f"Type of is_adult: {type(is_adult)}")

# ==============================================
# 4. OPERATORS - PERFORMING OPERATIONS
# ==============================================

print("\n⚙️ OPERATORS EXAMPLES:")

# Arithmetic operators
a = 15
b = 4

print(f"Numbers: a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Remainder: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"\nComparison operators:")
print(f"{a} == {b}: {a == b}")  # Equal to
print(f"{a} != {b}: {a != b}")  # Not equal to
print(f"{a} > {b}: {a > b}")    # Greater than
print(f"{a} < {b}: {a < b}")    # Less than
print(f"{a} >= {b}: {a >= b}")  # Greater than or equal
print(f"{a} <= {b}: {a <= b}")  # Less than or equal

# Logical operators
x = True
y = False

print(f"\nLogical operators:")
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")  # Both must be True
print(f"x or y: {x or y}")    # At least one must be True
print(f"not x: {not x}")      # Opposite of x

# ==============================================
# 5. USER INPUT AND OUTPUT
# ==============================================

print("\n💬 USER INPUT AND OUTPUT:")

# Getting input from user
print("Let's get some information about you!")

# Note: In a real program, you would uncomment these lines
# But for this demo, we'll use predetermined values

# user_name = input("What's your name? ")
# user_age = int(input("How old are you? "))
# favorite_color = input("What's your favorite color? ")

# For demo purposes, let's use these values:
user_name = "Student"
user_age = 20
favorite_color = "blue"

print(f"\nHello, {user_name}!")
print(f"You are {user_age} years old.")
print(f"Your favorite color is {favorite_color}.")

# Calculate some interesting facts
years_to_30 = 30 - user_age if user_age < 30 else 0
birth_year_estimated = 2025 - user_age

print(f"You were probably born in {birth_year_estimated}.")
if years_to_30 > 0:
    print(f"You'll turn 30 in {years_to_30} years.")
else:
    print("You're already 30 or older!")

# ==============================================
# 6. STRING OPERATIONS
# ==============================================

print("\n🔤 STRING OPERATIONS:")

# String methods
sample_text = "  Python Programming is Amazing!  "
print(f"Original: '{sample_text}'")
print(f"Uppercase: {sample_text.upper()}")
print(f"Lowercase: {sample_text.lower()}")
print(f"Trimmed: '{sample_text.strip()}'")
print(f"Length: {len(sample_text)} characters")
print(f"Replace 'Python' with 'Java': {sample_text.replace('Python', 'Java')}")
print(f"Starts with 'Python': {sample_text.strip().startswith('Python')}")
print(f"Contains 'Amazing': {'Amazing' in sample_text}")

# String formatting
name = "Alice"
score = 95.7
subject = "Python"

# Different ways to format strings
format1 = "Student " + name + " scored " + str(score) + " in " + subject
format2 = "Student {} scored {} in {}".format(name, score, subject)
format3 = f"Student {name} scored {score} in {subject}"  # f-string (recommended)

print(f"\nFormatting examples:")
print(f"Method 1: {format1}")
print(f"Method 2: {format2}")
print(f"Method 3: {format3}")

# ==============================================
# 7. BASIC MATH WITH PYTHON
# ==============================================

print("\n🧮 MATH OPERATIONS:")

import math  # Import math module for advanced functions

# Circle calculations
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\nTemperature conversions for {celsius}°C:")
print(f"Fahrenheit: {fahrenheit}°F")
print(f"Kelvin: {kelvin}K")

# Useful math functions
number = 16.7
print(f"\nMath functions for {number}:")
print(f"Square root: {math.sqrt(number):.2f}")
print(f"Ceiling: {math.ceil(number)}")
print(f"Floor: {math.floor(number)}")
print(f"Rounded: {round(number)}")

# ==============================================
# 8. PRACTICE EXERCISES FOR STUDENTS
# ==============================================

print("\n📝 PRACTICE EXERCISES:")
print("=" * 40)

print("""
EXERCISE 1: Personal Information
Create variables for:
- Your full name
- Your age
- Your favorite hobby
- Your dream job
Then print them in a nice format.
""")

# Example solution:
my_name = "John Smith"
my_age = 21
my_hobby = "reading"
my_dream_job = "software developer"

print(f"About me:")
print(f"Name: {my_name}")
print(f"Age: {my_age}")
print(f"Hobby: {my_hobby}")
print(f"Dream job: {my_dream_job}")

print("""
EXERCISE 2: Simple Calculator
Create a program that:
- Takes two numbers
- Performs all arithmetic operations
- Shows the results
""")

# Example solution:
num1 = 12
num2 = 5

print(f"\nCalculator for {num1} and {num2}:")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")

print("""
EXERCISE 3: Age Calculator
Calculate:
- How many days you've been alive
- How many hours you've been alive
- How many minutes you've been alive
""")

# Example solution:
age_years = 22
days_alive = age_years * 365
hours_alive = days_alive * 24
minutes_alive = hours_alive * 60

print(f"\nFor someone {age_years} years old:")
print(f"Days alive: {days_alive:,}")
print(f"Hours alive: {hours_alive:,}")
print(f"Minutes alive: {minutes_alive:,}")

# ==============================================
# 9. COMMON BEGINNER MISTAKES TO AVOID
# ==============================================

print("\n⚠️ COMMON MISTAKES TO AVOID:")

print("""
1. Variable Naming:
   ❌ Wrong: 1st_name, my-age, class
   ✅ Correct: first_name, my_age, student_class

2. String Concatenation:
   ❌ Wrong: "Age: " + age  (if age is a number)
   ✅ Correct: "Age: " + str(age) or f"Age: {age}"

3. Division:
   ❌ Confusing: 7 / 3 gives 2.333... (float division)
   ✅ Clear: 7 // 3 gives 2 (integer division)

4. Indentation:
   Python uses indentation to group code.
   Be consistent with spaces or tabs (prefer 4 spaces).
""")

# ==============================================
# 10. NEXT STEPS
# ==============================================

print("\n🚀 WHAT'S NEXT:")
print("""
In Week 2, we'll learn:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Functions and how to organize code
- Error handling basics

Keep practicing these basics - they're the foundation for everything else!

Homework:
1. Complete the practice exercises above
2. Try to create a program that calculates the tip for a restaurant bill
3. Make a program that converts between different units (meters to feet, etc.)
4. Experiment with different string methods and math operations
""")

print("\n🎉 Congratulations on completing Week 1 of Python basics!")
print("Remember: Practice makes perfect. Keep coding! 💪")

# ==============================================
# HOMEWORK SOLUTIONS (for instructors)
# ==============================================

def homework_solutions():
    """
    These are example solutions for the homework assignments.
    Students should try these on their own first.
    """
    
    print("\n" + "="*50)
    print("HOMEWORK SOLUTIONS (FOR INSTRUCTORS)")
    print("="*50)
    
    # Tip Calculator
    print("\n1. Tip Calculator:")
    bill_amount = 50.00
    tip_percentage = 18
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    
    print(f"Bill amount: ${bill_amount}")
    print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
    print(f"Total: ${total_amount:.2f}")
    
    # Unit Converter
    print("\n2. Unit Converter:")
    meters = 10
    feet = meters * 3.28084
    inches = feet * 12
    
    print(f"{meters} meters = {feet:.2f} feet = {inches:.2f} inches")
    
    # String Exploration
    print("\n3. String Methods Exploration:")
    text = "Python Programming"
    print(f"Original: {text}")
    print(f"Words: {text.split()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Character count: {len(text)}")
    print(f"Word count: {len(text.split())}")

# Uncomment the line below to see homework solutions
# homework_solutions()
