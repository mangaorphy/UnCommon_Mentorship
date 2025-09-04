/*
==============================================
INTERACTIVE JAVASCRIPT DEMO
==============================================
This file demonstrates how JavaScript interacts with HTML elements.
It's perfect for showing students how JavaScript brings websites to life!
*/

// Wait for the page to load before running JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log("🚀 Interactive JavaScript Demo Loaded!");
    
    // ==============================================
    // 1. DOM MANIPULATION - Interacting with HTML
    // ==============================================
    
    /*
    DOM (Document Object Model) represents the HTML structure.
    JavaScript can read and modify HTML elements through the DOM.
    */
    
    // Get references to HTML elements
    const greetButton = document.getElementById('greetButton');
    const greeting = document.getElementById('greeting');
    const nameInput = document.getElementById('nameInput');
    const personalGreetButton = document.getElementById('personalGreetButton');
    
    // Calculator elements
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const operationSelect = document.getElementById('operation');
    const calculateButton = document.getElementById('calculateButton');
    const resultDisplay = document.getElementById('result');
    
    // ==============================================
    // 2. EVENT LISTENERS - Responding to User Actions
    // ==============================================
    
    /*
    Event listeners allow JavaScript to respond to user interactions
    like clicks, typing, mouse movements, etc.
    */
    
    // Simple greeting button
    greetButton.addEventListener('click', function() {
        console.log("Greet button was clicked!");
        greeting.textContent = "Hello from JavaScript! 👋";
        greeting.style.color = "blue";
        greeting.style.fontSize = "18px";
        
        // Add some animation
        greeting.style.transform = "scale(1.1)";
        setTimeout(() => {
            greeting.style.transform = "scale(1)";
        }, 200);
    });
    
    // Personal greeting with user input
    personalGreetButton.addEventListener('click', function() {
        const userName = nameInput.value.trim();
        
        if (userName === "") {
            alert("Please enter your name first!");
            nameInput.focus(); // Put cursor in the input field
            return;
        }
        
        const personalMessage = `Hello, ${userName}! Welcome to JavaScript! 🎉`;
        greeting.textContent = personalMessage;
        greeting.style.color = "green";
        
        console.log(`Personal greeting for: ${userName}`);
        
        // Clear the input
        nameInput.value = "";
    });
    
    // Real-time input validation
    nameInput.addEventListener('input', function() {
        const value = nameInput.value;
        
        if (value.length > 0) {
            nameInput.style.borderColor = "green";
            personalGreetButton.disabled = false;
        } else {
            nameInput.style.borderColor = "";
            personalGreetButton.disabled = true;
        }
    });
    
    // ==============================================
    // 3. CALCULATOR FUNCTIONALITY
    // ==============================================
    
    /*
    This demonstrates how JavaScript can perform calculations
    and update the webpage dynamically.
    */
    
    // Calculator function (same as in script.js but modified for DOM)
    function calculate(operation, a, b) {
        const num1 = parseFloat(a);
        const num2 = parseFloat(b);
        
        if (isNaN(num1) || isNaN(num2)) {
            return "Please enter valid numbers";
        }
        
        switch (operation) {
            case "add":
                return num1 + num2;
            case "subtract":
                return num1 - num2;
            case "multiply":
                return num1 * num2;
            case "divide":
                if (num2 === 0) {
                    return "Cannot divide by zero!";
                }
                return num1 / num2;
            default:
                return "Invalid operation";
        }
    }
    
    // Calculator button event
    calculateButton.addEventListener('click', function() {
        const num1 = num1Input.value;
        const num2 = num2Input.value;
        const operation = operationSelect.value;
        
        console.log(`Calculating: ${num1} ${operation} ${num2}`);
        
        const result = calculate(operation, num1, num2);
        
        // Display result with formatting
        if (typeof result === 'number') {
            resultDisplay.textContent = `Result: ${result}`;
            resultDisplay.style.color = "blue";
        } else {
            resultDisplay.textContent = result; // Error message
            resultDisplay.style.color = "red";
        }
        
        // Log to console for learning
        console.log(`Result: ${result}`);
    });
    
    // Allow Enter key to trigger calculation
    [num1Input, num2Input].forEach(input => {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                calculateButton.click();
            }
        });
    });
    
    // ==============================================
    // 4. DYNAMIC CONTENT CREATION
    // ==============================================
    
    /*
    JavaScript can create new HTML elements and add them to the page.
    This is very powerful for creating dynamic, interactive websites.
    */
    
    // Create a tips section dynamically
    const tipsSection = document.createElement('div');
    tipsSection.className = 'js-tips';
    tipsSection.innerHTML = `
        <h3>🎯 JavaScript Learning Tips</h3>
        <ul id="tipsList">
            <li>Practice coding every day, even if it's just for 15 minutes</li>
            <li>Use console.log() to debug and understand your code</li>
            <li>Don't be afraid to make mistakes - they're part of learning!</li>
        </ul>
        <button id="addTipButton">Add Random Tip</button>
    `;
    
    // Add the tips section to the page
    const demoContainer = document.querySelector('.demo-container');
    demoContainer.appendChild(tipsSection);
    
    // Array of additional tips
    const additionalTips = [
        "Break complex problems into smaller, manageable pieces",
        "Read other people's code to learn different approaches",
        "Build projects that interest you to stay motivated",
        "Join coding communities and don't hesitate to ask questions",
        "Learn to use browser developer tools effectively",
        "Practice explaining code concepts to reinforce learning",
        "Start with simple projects and gradually increase complexity"
    ];
    
    // Add functionality to add random tips
    const addTipButton = document.getElementById('addTipButton');
    const tipsList = document.getElementById('tipsList');
    let usedTips = [];
    
    addTipButton.addEventListener('click', function() {
        if (usedTips.length >= additionalTips.length) {
            addTipButton.textContent = "All tips added! 🎉";
            addTipButton.disabled = true;
            return;
        }
        
        let randomTip;
        do {
            randomTip = additionalTips[Math.floor(Math.random() * additionalTips.length)];
        } while (usedTips.includes(randomTip));
        
        usedTips.push(randomTip);
        
        // Create and add new tip
        const newTip = document.createElement('li');
        newTip.textContent = randomTip;
        newTip.style.backgroundColor = "#f0f8ff";
        newTip.style.padding = "5px";
        newTip.style.marginTop = "5px";
        newTip.style.borderRadius = "3px";
        
        tipsList.appendChild(newTip);
        
        console.log(`Added tip: ${randomTip}`);
        
        // Update button text
        const remaining = additionalTips.length - usedTips.length;
        addTipButton.textContent = `Add Random Tip (${remaining} left)`;
    });
    
    // ==============================================
    // 5. DEMO OF JAVASCRIPT CONCEPTS IN ACTION
    // ==============================================
    
    console.log("\n=== LIVE JAVASCRIPT CONCEPTS DEMO ===");
    
    // Demonstrate different data types
    console.log("📊 Data Types Demo:");
    console.log("String:", typeof "Hello");
    console.log("Number:", typeof 42);
    console.log("Boolean:", typeof true);
    console.log("Array:", typeof [1, 2, 3]);
    console.log("Object:", typeof {name: "John"});
    
    // Demonstrate array methods
    console.log("\n📋 Array Methods Demo:");
    const fruits = ["apple", "banana", "orange"];
    console.log("Original fruits:", fruits);
    
    fruits.push("grape");
    console.log("After push:", fruits);
    
    const upperFruits = fruits.map(fruit => fruit.toUpperCase());
    console.log("Uppercase fruits:", upperFruits);
    
    const longFruits = fruits.filter(fruit => fruit.length > 5);
    console.log("Fruits with more than 5 letters:", longFruits);
    
    // Demonstrate object manipulation
    console.log("\n🏷️ Object Demo:");
    const student = {
        name: "Alex",
        age: 20,
        grades: [85, 92, 78, 96],
        isEnrolled: true
    };
    
    console.log("Student object:", student);
    console.log("Student name:", student.name);
    console.log("Average grade:", student.grades.reduce((sum, grade) => sum + grade, 0) / student.grades.length);
    
    // Demonstrate functions
    console.log("\n⚙️ Functions Demo:");
    
    const greetStudent = (name, course) => {
        return `Welcome ${name} to the ${course} course!`;
    };
    
    console.log(greetStudent("Emma", "JavaScript"));
    
    // Higher-order function example
    const processNumbers = (numbers, operation) => {
        return numbers.map(operation);
    };
    
    const numbers = [1, 2, 3, 4, 5];
    const doubled = processNumbers(numbers, x => x * 2);
    const squared = processNumbers(numbers, x => x ** 2);
    
    console.log("Original numbers:", numbers);
    console.log("Doubled:", doubled);
    console.log("Squared:", squared);
    
    // ==============================================
    // 6. PAGE INTERACTIONS AND EFFECTS
    // ==============================================
    
    // Add some visual feedback to all buttons
    const allButtons = document.querySelectorAll('button');
    allButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.2s';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
        
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 100);
        });
    });
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(event) {
        // Ctrl/Cmd + Enter to calculate
        if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
            calculateButton.click();
            console.log("Calculator triggered by keyboard shortcut!");
        }
        
        // Escape to clear all inputs
        if (event.key === 'Escape') {
            nameInput.value = '';
            num1Input.value = '';
            num2Input.value = '';
            greeting.textContent = '';
            resultDisplay.textContent = '';
            console.log("All inputs cleared!");
        }
    });
    
    console.log("\n🎮 Keyboard shortcuts:");
    console.log("- Ctrl/Cmd + Enter: Calculate");
    console.log("- Escape: Clear all inputs");
    
    console.log("\n✅ Interactive JavaScript Demo Ready!");
    console.log("Try interacting with the buttons and inputs on the page!");
});
