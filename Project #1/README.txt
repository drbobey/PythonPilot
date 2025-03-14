☕ Project: Café Order System
⏳ Duration: ~1 hour
 👥 Group Size: 4
 🛠️ Concepts Used:
 ✅ Variables & Data Types
 ✅ User Input
 ✅ Arithmetic Operations
 ✅ Assignment Operators
 ✅ String Formatting (f-strings, .format())

Overview
Welcome to the Café Order System project! In this assignment, you will build a simple text-based café ordering system using Python. The goal is to practice variables, data types, user input, arithmetic operations, assignment operators, and string formatting.
You will work in a group of 4, with each person responsible for a specific part of the program. By the end, your code will allow a user to enter their name, select a drink, entrée, and dessert, compute the total price with tax and tip, and print a formatted receipt.

🔀 Project Breakdown
Each team member will complete one task. The tasks are designed to connect smoothly, so work together to ensure consistency.

Task 1: User Input & Menu Display
📌 Goal: Create a simple café menu and greet the customer.
 ✅ What to do:
🔹Display a welcome message.
Format Example: Output something like "Welcome to Python Café!"
🔹Ask the user for their name.
Format Example: Output something like "What is your name?"
🔹Greet the user with their name.
Format Example: Output something like "Hi <name_var>, here is our menu!"
🔹Display the menu, listing drinks, entrées, and desserts with their prices.
Example: "Drinks: Coffee ($5), Tea ($5)..."

Task 2: Order Selection
📌 Goal: Ask the user what they’d like to order and store their choices.
 ✅ What to do:
🔹Ask the user what drink they would like.
Format Example: "Hi <name_var>, what would you like for your drink?"
🔹Ask for their entrée choice.
Format Example: "And what would you like for your entrée?"
🔹Ask for their dessert choice.
Format Example: "Finally, what would you like for dessert?"
🔹Store their choices in separate variables.

Task 3: Price Calculation & Receipt Formatting
📌 Goal: Compute the total cost and format the receipt.
 ✅ What to do:
🔹Assign fixed prices:
Drinks: $5
Entrées: $15
Desserts: $10
🔹Calculate the subtotal before tax.
🔹Compute a 10% tax on the subtotal.
🔹Compute a 15% tip on the subtotal.
🔹Compute the final total (subtotal + tax + tip).
🔹Format the receipt using string formatting (f-strings, .format(), etc.), but DO NOT print it yet—store it in a variable for later use.
Example format:
--- Python Café Receipt ---  
Name: <name_var>  
Drink: <drink_var> - $5  
Entrée: <entrée_var> - $15  
Dessert: <dessert_var> - $10  
--------------------------  
Subtotal: $XX.XX  
Tax (10%): $XX.XX  
Tip (15%): $XX.XX  
Total: $XX.XX  
--------------------------  
Thank you for dining with us!  

Task 4: Final Order Summary & Confirmation
📌 Goal: Recap the order and display the receipt.
 ✅ What to do:
🔹Recap the user’s order before showing the total.
Format Example: "So, <name_var>, you ordered <drink_var>, <entrée_var>, and <dessert_var>."
🔹Display the receipt stored in Task 3.
🔹Print a final thank-you message.
Format Example: "Thank you for dining at Python Café, <name_var>! Enjoy your meal!"

🤝 Collaboration & Integration Guide
✔ Use consistent variable names (user_name, drink_choice, total_price, etc.).
✔ Test each section individually before merging everything together.
✔ Ensure formatted output using f-strings for clarity.
✔ The person working on Task 4 should verify the receipt formatting for accuracy.

