"""
==============================================
WEEK 2: CONTROL FLOW AND FUNCTIONS
==============================================
This file contains practical examples and exercises for Week 2 topics:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Loop control (break, continue)
- Functions: definition, parameters, return values
- Variable scope (local vs global)
- Lambda functions (introduction)
- Error handling basics (try/except)
"""

print("🐍 Week 2: Control Flow and Functions")
print("=" * 50)

# ==============================================
# 1. CONDITIONAL STATEMENTS (if, elif, else)
# ==============================================

print("\n🔀 CONDITIONAL STATEMENTS")
print("-" * 30)

# Basic if statement
age = 20 
if age >= 18:
    print(f"Age {age}: You are an adult!")
else:
    print("Still")
# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside! 🌞")
else:
    print("It's comfortable or cool outside. 😊")

# if-elif-else chain
score = 85
print(f"\nGrade for score {score}:")
if score >= 90:
    grade = "A"
    print("Excellent work! 🌟")
elif score >= 80:
    grade = "B"
    print("Good job! 👍")
elif score >= 70:
    grade = "C"
    print("You passed! ✅")
elif score >= 60:
    grade = "D"
    print("You need to improve. 📚")
else:
    grade = "F"
    print("Please study harder. 💪")

print(f"Your grade is: {grade}")

# Multiple conditions
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Welcome, Administrator!")
elif username == "admin" and password != "secret123":
    print("Wrong password!")
elif username != "admin":
    print("User not found!")

# Nested conditions
weather = "sunny"
have_umbrella = True # Boolean

if weather == "rainy":
    if have_umbrella:
        print("You're prepared for the rain! ☂️")
    else:
        print("You might get wet! 🌧️")
else:
    print("Enjoy the nice weather! ☀️")

# ==============================================
# 2. LOOPS - FOR LOOPS
# ==============================================

print("\n🔄 FOR LOOPS")
print("-" * 15)

# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# List
# Dictionaries 
person = {
    "name": "Tadiwa", "age": "18"
}
person[age]
person[1]
# Sets

# Loop through a list
fruits = ["apple", "banana", "orange", "grape"]
print(f"\nFruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index using enumerate
print(f"\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Loop through a dictionary
student_grades = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 85,
    "Diana": 96
}

print(f"\nStudent grades:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

# Nested loops - multiplication table
print(f"\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result:2d}", end="  ")
    print()  # New line after each row

# ==============================================
# 3. LOOPS - WHILE LOOPS
# ==============================================

print("\n🔁 WHILE LOOPS")
print("-" * 16)

# Basic while loop
print("Countdown:")
count = 5
while count > 0:
    print(f"{count}...")
    count -= 1
print("Blast off! 🚀")

# While loop with user input simulation
print(f"\nPassword attempt simulation:")
attempts = 0
max_attempts = 3
correct_password = "python123"

# Simulating user attempts (in real program, use input())
user_attempts = ["wrong1", "wrong2", "python123"]

while attempts < max_attempts:
    # In real program: password = input("Enter password: ")
    password = user_attempts[attempts] if attempts < len(user_attempts) else "wrong"
    attempts += 1
    
    if password == correct_password:
        print("Access granted! ✅")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Account locked! ❌")

# ==============================================
# 4. LOOP CONTROL (break, continue)
# ==============================================

print("\n⏸️ LOOP CONTROL: break and continue")
print("-" * 40)

# Using 'continue' to skip iterations
print("Even numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 != 0:  # If odd number
        continue      # Skip to next iteration
    print(f"{num} is even")

# Using 'break' to exit early
print(f"\nFinding first number divisible by 7:")
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Found it: {num}")
        break
    print(f"Checking {num}...")

# Combining break and continue
print(f"\nProcessing numbers 1-20 (skip multiples of 3, stop at first multiple of 13):")
for num in range(1, 21):
    if num % 13 == 0:
        print(f"Found multiple of 13: {num}. Stopping!")
        break
    if num % 3 == 0:
        print(f"Skipping {num} (multiple of 3)")
        continue
    print(f"Processing {num}")

# ==============================================
# 5. FUNCTIONS - DEFINITION, PARAMETERS, RETURN VALUES
# ==============================================

print("\n🔧 FUNCTIONS")
print("-" * 12)

# Simple function with no parameters
def greet():
    """A simple greeting function"""
    return "Hello, Welcome to Python!"

print("Simple function:")
message = greet()
print(message)

# Function with parameters
def greet_person(name, age):
    """Greet a person with their name and age"""
    return f"Hello {name}! You are {age} years old."

print(f"\nFunction with parameters:")
greeting = greet_person("Alice", 25)
print(greeting)

# Function with default parameters
def introduce(name, age, city="Unknown"):
    """Introduction with default city"""
    return f"Hi, I'm {name}, {age} years old, from {city}."

print(f"\nFunction with default parameters:")
print(introduce("Bob", 30))
print(introduce("Charlie", 28, "New York"))

# Function with multiple return values
def calculate_rectangle(length, width):
    """Calculate area and perimeter of rectangle"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print(f"\nFunction with multiple return values:")
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"Rectangle (5x3): Area = {rect_area}, Perimeter = {rect_perimeter}")

# Function with variable arguments
def calculate_average(*numbers):
    """Calculate average of any number of values"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(f"\nFunction with variable arguments:")
avg1 = calculate_average(10, 20, 30)
avg2 = calculate_average(5, 15, 25, 35, 45)
print(f"Average of (10,20,30): {avg1}")
print(f"Average of (5,15,25,35,45): {avg2}")

# Function with keyword arguments
def create_profile(**info):
    """Create user profile from keyword arguments"""
    profile = "User Profile:\n"
    for key, value in info.items():
        profile += f"  {key.title()}: {value}\n"
    return profile

print(f"\nFunction with keyword arguments:")
profile = create_profile(name="John", age=30, city="Boston", hobby="reading")
print(profile)

# ==============================================
# 6. VARIABLE SCOPE (local vs global)
# ==============================================

print("\n🌍 VARIABLE SCOPE")
print("-" * 18)

# Global variable
global_counter = 0

def demonstrate_scope():
    """Demonstrate local vs global scope"""
    # Local variable
    local_counter = 10
    print(f"Inside function - local_counter: {local_counter}")
    print(f"Inside function - global_counter: {global_counter}")

def modify_global():
    """Modify global variable"""
    global global_counter
    global_counter += 1
    print(f"Global counter modified to: {global_counter}")

def local_vs_global():
    """Show local variable shadowing global"""
    global_counter = 999  # This creates a local variable!
    print(f"Local global_counter (shadows global): {global_counter}")

print("Scope demonstration:")
demonstrate_scope()
modify_global()
local_vs_global()
print(f"After all functions, global_counter is: {global_counter}")

# Practical example: Bank account
account_balance = 1000  # Global variable

def deposit(amount):
    """Deposit money to account"""
    global account_balance
    if amount > 0:
        account_balance += amount
        return f"Deposited ${amount}. New balance: ${account_balance}"
    return "Invalid deposit amount"

def withdraw(amount):
    """Withdraw money from account"""
    global account_balance
    if amount > 0 and amount <= account_balance:
        account_balance -= amount
        return f"Withdrew ${amount}. New balance: ${account_balance}"
    return "Invalid withdrawal amount or insufficient funds"

def check_balance():
    """Check current balance"""
    return f"Current balance: ${account_balance}"

print(f"\nBank account example:")
print(check_balance())
print(deposit(200))
print(withdraw(150))
print(check_balance())

# ==============================================
# 7. LAMBDA FUNCTIONS (INTRODUCTION)
# ==============================================

print("\n⚡ LAMBDA FUNCTIONS")
print("-" * 19)

# Basic lambda function
square = lambda x: x ** 2
print(f"Lambda to square number:")
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
multiply = lambda x, y, z: x * y * z

print(f"\nLambda with multiple parameters:")
print(f"add(3, 7) = {add(3, 7)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nUsing lambda with filter:")
print(f"Even numbers: {even_numbers}")

# Map - square all numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"\nUsing lambda with map:")
print(f"Squared numbers: {squared_numbers}")

# Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 96)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(f"\nUsing lambda with sorted:")
print(f"Students sorted by grade: {sorted_by_grade}")

# Practical lambda examples
# Temperature converter
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

print(f"\nTemperature converters:")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_to_celsius(77)}°C")

# ==============================================
# 8. ERROR HANDLING BASICS (try/except)
# ==============================================

print("\n🛡️ ERROR HANDLING")
print("-" * 18)

# Basic try-except
print("Basic error handling:")
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling multiple exception types
print(f"\nHandling multiple exception types:")
def safe_divide(a, b):
    try:
        result = a / b
        return f"{a} ÷ {b} = {result}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"
    except TypeError:
        return "Error: Please provide numeric values!"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "abc"))

# try-except-else-finally
print(f"\nComplete try-except-else-finally:")
def process_file(filename):
    try:
        # Simulate file operations
        if filename == "valid.txt":
            data = "File content here"
            print(f"Successfully read {filename}")
            return data
        else:
            raise FileNotFoundError("File not found")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    else:
        print("File processed successfully!")
    finally:
        print("Cleaning up resources...")

print("Processing valid file:")
process_file("valid.txt")
print("\nProcessing invalid file:")
process_file("invalid.txt")

# Practical error handling example
def get_user_age():
    """Get user age with error handling"""
    # Simulating user input (in real program, use input())
    user_inputs = ["25", "abc", "-5", "30"]
    
    for user_input in user_inputs:
        print(f"\nTrying input: '{user_input}'")
        try:
            age = int(user_input)
            if age < 0:
                raise ValueError("Age cannot be negative")
            if age > 150:
                raise ValueError("Age seems unrealistic")
            print(f"Valid age entered: {age}")
            return age
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid number")
            else:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

get_user_age()

# ==============================================
# 9. PRACTICAL EXERCISES AND EXAMPLES
# ==============================================

print("\n\n📝 PRACTICAL EXERCISES")
print("=" * 25)

# Exercise 1: Grade Calculator with Functions
def calculate_letter_grade(score):
    """Calculate letter grade from numeric score"""
    try:
        score = float(score)
        if score < 0 or score > 100:
            return "Error: Score must be between 0 and 100"
        
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Error: Invalid score format"

print("Exercise 1: Grade Calculator")
test_scores = [95, 83, 77, 65, 45, "invalid", 105]
for score in test_scores:
    grade = calculate_letter_grade(score)
    print(f"Score {score}: Grade {grade}")

# Exercise 2: Number Guessing Game
import random

def number_guessing_game():
    """Simple number guessing game"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    # Simulated guesses for demo
    guesses = [50, 75, 63, 69, 67, 68]
    
    print(f"\nExercise 2: Number Guessing Game")
    print(f"Guess the number between 1 and 100!")
    print(f"You have {max_attempts} attempts.")
    
    for guess in guesses:
        attempts += 1
        print(f"\nAttempt {attempts}: Guessing {guess}")
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You found it in {attempts} attempts!")
            return
        elif guess < secret_number:
            print("Too low! 📈")
        else:
            print("Too high! 📉")
        
        if attempts >= max_attempts:
            print(f"💔 Game over! The number was {secret_number}")
            return
        
        remaining = max_attempts - attempts
        print(f"You have {remaining} attempts left.")

number_guessing_game()

# Exercise 3: Text Analyzer with Multiple Functions
def analyze_text(text):
    """Comprehensive text analysis"""
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        
        # Basic statistics
        char_count = len(text)
        word_count = len(text.split())
        sentence_count = text.count('.') + text.count('!') + text.count('?')
        
        # Character frequency (using lambda and dict comprehension)
        char_freq = {}
        for char in text.lower():
            if char.isalpha():
                char_freq[char] = char_freq.get(char, 0) + 1
        
        # Most common character
        if char_freq:
            most_common = max(char_freq.items(), key=lambda x: x[1])
        else:
            most_common = ("None", 0)
        
        return {
            "characters": char_count,
            "words": word_count,
            "sentences": sentence_count,
            "most_common_letter": most_common[0],
            "letter_frequency": most_common[1]
        }
    
    except Exception as e:
        return {"error": str(e)}

print(f"\nExercise 3: Text Analyzer")
sample_text = "Hello world! This is a sample text for analysis. How many words and characters are here?"
analysis = analyze_text(sample_text)
print(f"Text: '{sample_text}'")
print("Analysis results:")
for key, value in analysis.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")

# ==============================================
# 10. HOMEWORK ASSIGNMENTS
# ==============================================

print(f"\n\n📚 HOMEWORK ASSIGNMENTS")
print("=" * 26)

homework_problems = """
HOMEWORK FOR WEEK 2:

1. PASSWORD VALIDATOR:
   Create a function that validates passwords with these rules:
   - At least 8 characters long
   - Contains both uppercase and lowercase letters
   - Contains at least one digit
   - Contains at least one special character (@, #, $, %)
   Use try-except to handle errors gracefully.

2. SHOPPING CART CALCULATOR:
   Create a program that:
   - Uses a loop to add items to a shopping cart
   - Each item has a name and price
   - Calculates total with tax (use a function)
   - Applies discounts based on total amount
   - Uses lambda functions for tax and discount calculations

3. FIBONACCI SEQUENCE GENERATOR:
   Write a function that generates Fibonacci numbers:
   - Use both iterative (loop) and recursive approaches
   - Include error handling for invalid inputs
   - Stop generation when numbers exceed a given limit

4. STUDENT GRADE MANAGEMENT:
   Create a system that:
   - Stores student names and their grades
   - Calculates class average, highest, and lowest grades
   - Uses functions for all calculations
   - Handles errors when student not found
   - Uses lambda functions for sorting students by grade

5. SIMPLE CALCULATOR:
   Build a calculator that:
   - Uses functions for each operation (+, -, *, /, %, **)
   - Has a menu system with loops
   - Includes comprehensive error handling
   - Allows users to continue or exit
   - Keeps history of calculations
"""

print(homework_problems)

# ==============================================
# SOLUTIONS PREVIEW (for instructors)
# ==============================================

def instructor_solutions():
    """Preview of homework solutions for instructors"""
    
    print("\n" + "="*50)
    print("INSTRUCTOR SOLUTIONS PREVIEW")
    print("="*50)
    
    # Solution 1: Password Validator
    def validate_password(password):
        try:
            if len(password) < 8:
                return False, "Password too short"
            if not any(c.isupper() for c in password):
                return False, "Missing uppercase letter"
            if not any(c.islower() for c in password):
                return False, "Missing lowercase letter"
            if not any(c.isdigit() for c in password):
                return False, "Missing digit"
            if not any(c in "@#$%" for c in password):
                return False, "Missing special character"
            return True, "Password is valid"
        except Exception as e:
            return False, f"Error: {e}"
    
    print("\n1. Password Validator Example:")
    test_passwords = ["weak", "StrongPass1@", "nodigits@", "NOLOWER1@"]
    for pwd in test_passwords:
        is_valid, message = validate_password(pwd)
        print(f"'{pwd}': {message}")
    
    # Solution 2: Fibonacci Generator
    def fibonacci_iterative(limit):
        try:
            if limit <= 0:
                return []
            
            fib_sequence = []
            a, b = 0, 1
            
            while a <= limit:
                fib_sequence.append(a)
                a, b = b, a + b
            
            return fib_sequence
        except Exception as e:
            return f"Error: {e}"
    
    print(f"\n2. Fibonacci Generator (up to 100):")
    fib_nums = fibonacci_iterative(100)
    print(f"Fibonacci numbers: {fib_nums}")

# Uncomment to see instructor solutions
# instructor_solutions()

print(f"\n🎉 End of Week 2: Control Flow and Functions!")
print("Keep practicing these concepts - they're the building blocks of programming! 💪")

# ==============================================
# SUMMARY OF KEY CONCEPTS
# ==============================================

summary = """
📋 WEEK 2 SUMMARY - KEY CONCEPTS:

✅ CONDITIONALS (if/elif/else):
   - Make decisions in your code
   - Use comparison and logical operators
   - Can be nested for complex logic

✅ LOOPS:
   - FOR: When you know how many iterations
   - WHILE: When you loop until a condition is met
   - Use break/continue to control loop flow

✅ FUNCTIONS:
   - Organize code into reusable blocks
   - Can take parameters and return values
   - Help make code more readable and maintainable

✅ VARIABLE SCOPE:
   - Local variables exist only inside functions
   - Global variables can be accessed anywhere
   - Use 'global' keyword to modify global variables

✅ LAMBDA FUNCTIONS:
   - Short, anonymous functions
   - Useful for simple operations
   - Great with map(), filter(), sorted()

✅ ERROR HANDLING:
   - Use try/except to handle errors gracefully
   - Different exception types for different errors
   - Always plan for things that might go wrong

🎯 NEXT WEEK: Data Structures (Lists, Dictionaries, Sets)
"""

print(summary)