import random  # Importing random module for dice rolls

# 🎲 Dice-Based Racing Game - Code Framework

# Task 1: Game Setup
# TODO: Print a welcome message introducing the game.
# TODO: Ask Player 1 for their name and store it in a variable.
# TODO: Ask Player 2 for their name and store it in a variable.
# TODO: Initialize both players' scores to 0.
# TODO: Display the starting scores for both players.
# TODO: Set up a variable to track whose turn it is (Player 1 starts).
# HINT: Use a numeric flag (e.g., 1 or 2) to represent the current player.
# TODO: Create a while loop to contain the game logic. 
# HINT: Use the while(True) condition.

# Task 2: Player Turn & Dice Roll
# TODO: Prompt the current player to press Enter to roll the dice.
dice_roll = random.randint(1, 6)  # Generates a random number between 1 and 6
# TODO: Display the result of the dice roll.
# TODO: Add the dice roll result to the current player's score.
# HINT: Use a temporary variable to hold the current score, update it, then store it back.

# Task 3: Special Race Events
# TODO: If the player rolls a 6, print a message and allow an extra roll.
# TODO: If the player rolls a 1, print a message and subtract 2 points (ensure score doesn't go below 0).
# TODO: If the player's score reaches exactly 15, print a message and add a 5-point turbo boost.
# HINT: Make sure to check these conditions immediately after rolling or updating the score.

# Task 4: Checking for a Winner & Ending the Game
# TODO: After each turn, check if the player's score is 20 or more.
# TODO: If a player reaches 20 or more points, print a message declaring them the winner and end the game.
# HINT: Use a condition to break out of the game loop when a player wins.

# Task 5: Turn Management & Game Continuation
# TODO: Switch turn to the next player after each roll.
# HINT: Use if-else or a conditional toggle to change the current player's turn.
# TODO: Ensure turns alternate correctly between players.
# TODO: At the end of the game, display a final message .

