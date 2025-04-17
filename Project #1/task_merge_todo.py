"""
Task 5: Merging & Integration
📌 Goal: Combine all sections into a working program.

✅ What to do:
1. Ensure the user input from Task 1 flows into Task 2.
   - The name should be stored and used throughout the program.

2. Pass the user’s selected menu choices from Task 2 to Task 3.
   - The drink, entrée, and dessert choices should be consistent.

3. Ensure Task 3 correctly calculates and formats the receipt.

4. The formatted receipt from Task 3 should be displayed correctly in Task 4.

5. Test the entire program for errors, ensuring all user inputs and outputs work smoothly.

6. As a team, review and refine the final program to ensure clarity and a smooth user experience.

"""

print("Welcome to Python Café!") 

nameCustomer = input("What is your name?")   

print(f"Hi {nameCustomer} , here is our menu!") 

print("Coffee ($5)" )
print("Tea ($5)" )
print("Weed ($5)" )
print("Alcohol ($5)" )

drink=input(f"Hi {nameCustomer}, what would you like for your drink?")
entrée=input("And what would you like for your entrée?")
dessert=input("Finally, what would you like for dessert?")

drinkPrice = 5
entreePrice = 15
dessertPrice = 10

totalPriceBeforeTax = drinkPrice + entreePrice + dessertPrice

taxValue = 0.1 * totalPriceBeforeTax

tipValue = 0.15 * totalPriceBeforeTax

totalPrice = totalPriceBeforeTax + taxValue + tipValue

output = f"""
   --- Python Café Receipt ---  
   Name: ${nameCustomer} 
   Drink:  ${drink} - $5  
   Entrée: ${entrée} - $15  
   Dessert: ${dessert} - $10  
   --------------------------  
   Subtotal: ${totalPriceBeforeTax:.2f} 
   Tax (10%): ${taxValue:.2f} 
   Tip (15%): ${tipValue:.1f} 
   Total: ${totalPrice:.2f}
   --------------------------  
   Thank you for dining with us!  
"""

print(f"Customer {nameCustomer}, you ordered {drink}, {entrée}, and {dessert}.")
print(output)
print(f"Thank you for dining at Python Café,{nameCustomer}! Enjoy your meal!")