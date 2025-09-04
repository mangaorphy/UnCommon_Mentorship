/*
==============================================
JAVASCRIPT BASICS TUTORIAL
==============================================
This file contains fundamental JavaScript concepts with clear explanations and examples.
Perfect for teaching someone new to programming.
*/

// ==============================================
// 1. VARIABLES - Storing Information
// ==============================================

/*
Variables are containers that store data.
Think of them like labeled boxes where you can put information.
*/

// Different ways to declare variables:
var oldWay = "This is the old way (avoid using)";
let modernWay = "This is the modern way";
const constantValue = "This value cannot be changed";

// Variable naming rules:
let userName = "John";          // Good: camelCase
let user_age = 25;              // Okay: snake_case
let isLoggedIn = true;          // Good: descriptive names
// let 123invalid;              // Error: can't start with number
// let my-variable;             // Error: no hyphens allowed

console.log("=== VARIABLES EXAMPLES ===");
console.log("User name:", userName);
console.log("User age:", user_age);
console.log("Is logged in:", isLoggedIn);

// ==============================================
// 2. DATA TYPES - Different Kinds of Information
// ==============================================

/*
JavaScript has several data types to represent different kinds of information:
*/

// PRIMITIVE DATA TYPES:

// String - Text data
let firstName = "Alice";
let lastName = 'Smith';
let fullName = `${firstName} ${lastName}`; // Template literal

// Number - Numeric data (integers and decimals)
let age = 30;
let price = 19.99;
let temperature = -5;

// Boolean - True or False
let isStudent = true;
let isRetired = false;

// Undefined - Variable declared but no value assigned
let notAssigned;

// Null - Intentionally empty value
let emptyValue = null;

console.log("\n=== DATA TYPES EXAMPLES ===");
console.log("String:", fullName, "- Type:", typeof fullName);
console.log("Number:", age, "- Type:", typeof age);
console.log("Boolean:", isStudent, "- Type:", typeof isStudent);
console.log("Undefined:", notAssigned, "- Type:", typeof notAssigned);
console.log("Null:", emptyValue, "- Type:", typeof emptyValue);

// ==============================================
// 3. OPERATORS - Performing Operations
// ==============================================

/*
Operators allow you to perform operations on variables and values.
*/

// ARITHMETIC OPERATORS
let a = 10;
let b = 3;

console.log("\n=== ARITHMETIC OPERATORS ===");
console.log("Addition:", a + b);        // 13
console.log("Subtraction:", a - b);     // 7
console.log("Multiplication:", a * b);  // 30
console.log("Division:", a / b);        // 3.333...
console.log("Remainder:", a % b);       // 1
console.log("Exponentiation:", a ** b); // 1000

// COMPARISON OPERATORS
console.log("\n=== COMPARISON OPERATORS ===");
console.log("Equal:", a == b);          // false
console.log("Strictly equal:", a === b); // false
console.log("Not equal:", a != b);      // true
console.log("Greater than:", a > b);    // true
console.log("Less than:", a < b);       // false
console.log("Greater or equal:", a >= b); // true

// LOGICAL OPERATORS
let x = true;
let y = false;

console.log("\n=== LOGICAL OPERATORS ===");
console.log("AND:", x && y);            // false
console.log("OR:", x || y);             // true
console.log("NOT:", !x);                // false

// ==============================================
// 4. CONDITIONALS - Making Decisions
// ==============================================

/*
Conditionals allow your program to make decisions and execute different code
based on different conditions.
*/

let score = 85;

console.log("\n=== CONDITIONALS EXAMPLES ===");

// IF-ELSE STATEMENT
if (score >= 90) {
    console.log("Grade: A - Excellent!");
} else if (score >= 80) {
    console.log("Grade: B - Good job!");
} else if (score >= 70) {
    console.log("Grade: C - Not bad!");
} else if (score >= 60) {
    console.log("Grade: D - Need improvement!");
} else {
    console.log("Grade: F - Study harder!");
}

// TERNARY OPERATOR (shorter way to write simple if-else)
let status = age >= 18 ? "Adult" : "Minor";
console.log("Status:", status);

// SWITCH STATEMENT (good for multiple specific values)
let day = "Monday";
let message;

switch (day) {
    case "Monday":
        message = "Start of the work week!";
        break;
    case "Friday":
        message = "TGIF!";
        break;
    case "Saturday":
    case "Sunday":
        message = "Weekend time!";
        break;
    default:
        message = "Regular day";
}
console.log("Day message:", message);

// ==============================================
// 5. LOOPS - Repeating Actions
// ==============================================

/*
Loops allow you to repeat code multiple times without writing it over and over.
*/

console.log("\n=== LOOPS EXAMPLES ===");

// FOR LOOP - when you know how many times to repeat
console.log("FOR LOOP - Counting 1 to 5:");
for (let i = 1; i <= 5; i++) {
    console.log("Count:", i);
}

// WHILE LOOP - when you don't know exact number of repetitions
console.log("\nWHILE LOOP - Countdown from 5:");
let countdown = 5;
while (countdown > 0) {
    console.log("Countdown:", countdown);
    countdown--;
}

// FOR...OF LOOP - for iterating through arrays
let colors = ["red", "green", "blue"];
console.log("\nFOR...OF LOOP - Colors:");
for (let color of colors) {
    console.log("Color:", color);
}

// ==============================================
// 6. ARRAYS - Lists of Data
// ==============================================

/*
Arrays are ordered lists that can store multiple values.
Think of them like a shopping list or a playlist.
*/

console.log("\n=== ARRAYS EXAMPLES ===");

// Creating arrays
let fruits = ["apple", "banana", "orange"];
let numbers = [1, 2, 3, 4, 5];
let mixed = ["John", 25, true, null];

console.log("Fruits array:", fruits);
console.log("First fruit:", fruits[0]);    // Arrays start at index 0
console.log("Array length:", fruits.length);

// Array methods (functions that work on arrays)
fruits.push("grape");           // Add to end
console.log("After push:", fruits);

fruits.pop();                   // Remove from end
console.log("After pop:", fruits);

fruits.unshift("mango");        // Add to beginning
console.log("After unshift:", fruits);

let foundIndex = fruits.indexOf("banana");
console.log("Index of banana:", foundIndex);

// ==============================================
// 7. OBJECTS - Structured Data
// ==============================================

/*
Objects are collections of key-value pairs.
Think of them like a filing cabinet where each file has a label (key) and content (value).
*/

console.log("\n=== OBJECTS EXAMPLES ===");

// Creating an object
let person = {
    name: "Sarah",
    age: 28,
    city: "New York",
    isEmployed: true,
    hobbies: ["reading", "swimming", "coding"]
};

console.log("Person object:", person);
console.log("Person's name:", person.name);        // Dot notation
console.log("Person's age:", person["age"]);       // Bracket notation

// Adding new properties
person.email = "sarah@email.com";
person["phone"] = "123-456-7890";

console.log("Updated person:", person);

// ==============================================
// 8. FUNCTIONS - Reusable Code Blocks
// ==============================================

/*
Functions are reusable blocks of code that perform specific tasks.
Think of them like recipes - you write them once and use them many times.
*/

console.log("\n=== FUNCTIONS EXAMPLES ===");

// Function declaration
function greet(name) {
    return `Hello, ${name}! Welcome to JavaScript!`;
}

// Function expression
const add = function(x, y) {
    return x + y;
};

// Arrow function (modern syntax)
const multiply = (x, y) => x * y;

// Using functions
console.log(greet("Alice"));
console.log("5 + 3 =", add(5, 3));
console.log("4 * 6 =", multiply(4, 6));

// Function with multiple parameters and complex logic
function calculateGrade(score) {
    if (score >= 90) return "A";
    if (score >= 80) return "B";
    if (score >= 70) return "C";
    if (score >= 60) return "D";
    return "F";
}

console.log("Score 95 gets grade:", calculateGrade(95));
console.log("Score 73 gets grade:", calculateGrade(73));

// ==============================================
// 9. SCOPE - Where Variables Live
// ==============================================

/*
Scope determines where variables can be accessed in your code.
*/

console.log("\n=== SCOPE EXAMPLES ===");

let globalVariable = "I can be accessed anywhere";

function scopeExample() {
    let localVariable = "I only exist inside this function";
    console.log("Inside function - Global:", globalVariable);
    console.log("Inside function - Local:", localVariable);
    
    if (true) {
        let blockVariable = "I only exist inside this block";
        console.log("Inside block:", blockVariable);
    }
    
    // console.log(blockVariable); // This would cause an error!
}

scopeExample();
console.log("Outside function - Global:", globalVariable);
// console.log(localVariable); // This would cause an error!

// ==============================================
// 10. COMMON BUILT-IN METHODS
// ==============================================

console.log("\n=== BUILT-IN METHODS EXAMPLES ===");

// String methods
let text = "  JavaScript is Amazing!  ";
console.log("Original:", `"${text}"`);
console.log("Uppercase:", text.toUpperCase());
console.log("Lowercase:", text.toLowerCase());
console.log("Trimmed:", `"${text.trim()}"`);
console.log("Length:", text.length);
console.log("Includes 'Script':", text.includes("Script"));

// Math methods
console.log("Random number:", Math.random());
console.log("Round 4.7:", Math.round(4.7));
console.log("Max of 5, 10, 3:", Math.max(5, 10, 3));
console.log("Square root of 16:", Math.sqrt(16));

// Date methods
let now = new Date();
console.log("Current date:", now);
console.log("Current year:", now.getFullYear());
console.log("Current month:", now.getMonth() + 1); // +1 because months start at 0

// ==============================================
// 11. ERROR HANDLING
// ==============================================

console.log("\n=== ERROR HANDLING EXAMPLES ===");

// Try-catch for handling errors gracefully
function safeDivision(a, b) {
    try {
        if (b === 0) {
            throw new Error("Cannot divide by zero!");
        }
        return a / b;
    } catch (error) {
        console.log("Error caught:", error.message);
        return null;
    }
}

console.log("10 / 2 =", safeDivision(10, 2));
console.log("10 / 0 =", safeDivision(10, 0));

// ==============================================
// PRACTICE EXERCISES
// ==============================================

console.log("\n=== PRACTICE EXERCISES ===");

// Exercise 1: Create a function that checks if a number is even or odd
function isEven(number) {
    return number % 2 === 0;
}

console.log("Is 4 even?", isEven(4));
console.log("Is 7 even?", isEven(7));

// Exercise 2: Create a function that finds the largest number in an array
function findLargest(numbers) {
    let largest = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
    }
    return largest;
}

let testNumbers = [3, 7, 2, 9, 1, 8];
console.log("Largest number in", testNumbers, "is:", findLargest(testNumbers));

// Exercise 3: Create a simple calculator
function calculator(operation, a, b) {
    switch (operation) {
        case "add":
            return a + b;
        case "subtract":
            return a - b;
        case "multiply":
            return a * b;
        case "divide":
            return b !== 0 ? a / b : "Cannot divide by zero";
        default:
            return "Invalid operation";
    }
}

console.log("Calculator 5 + 3 =", calculator("add", 5, 3));
console.log("Calculator 10 - 4 =", calculator("subtract", 10, 4));
console.log("Calculator 6 * 7 =", calculator("multiply", 6, 7));

console.log("\n=== END OF JAVASCRIPT BASICS TUTORIAL ===");
console.log("Congratulations! You've learned the fundamentals of JavaScript!");
