"""
Task 3: Price Calculation & Receipt Formatting
📌 Goal: Compute the total cost and format the receipt.

✅ What to do:
1. Assign fixed prices:
   - Drinks: $5
   - Entrées: $15
   - Desserts: $10

2. Calculate the subtotal before tax.

3. Compute a 10% tax on the subtotal.

4. Compute a 15% tip on the subtotal.

5. Compute the final total (subtotal + tax + tip).

6. Format the receipt using string formatting (f-strings, .format(), etc.), but DO NOT print it yet—store it in a variable for later use.

   Example format:
   --------------------------
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

"""

drinkPrice = 5
entreePrice = 15
dessertPrice = 10

#Guesswork
drinkSelected = 0 # 1 if selected
entreeSelected = 0 # 1 if selected
dessertSelected = 0 # 1 if selected

totalPriceBeforeTax = drinkPrice * drinkSelected + entreePrice * entreeSelected + dessertPrice * dessertSelected

taxValue = 10 / 100 * totalPriceBeforeTax

tipValue = 15 / 100 * totalPriceBeforeTax

totalPrice = totalPriceBeforeTax + taxValue + tipValue

output = f"""
   --- Python Café Receipt ---  
   Name: ${nameCustomer} 
   Drink:  ${drinkSelected} - $5  
   Entrée: ${entreeSelected} - $15  
   Dessert: ${dessertSelected} - $10  
   --------------------------  
   Subtotal: ${totalPriceBeforeTax:.2f} 
   Tax (10%): ${taxValue:.2f} 
   Tip (15%): ${tipValue:.2f} 
   Total: ${totalPrice:.2f}
   --------------------------  
   Thank you for dining with us!  
"""

