'''
Adventure Game
Author: Armando Guzman
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Welcome message and introduction
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# Ask for the players name
player_name = input('what is your name, adventurer?')

#Concatenate strings to creat a personalized message
print("welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("do you wish to take the path (yes or no): ").lower()

# Respond based on the player's decision
if decision == "yes":
    print(f"brave choice, {player_name}! You step on the path and venture forward")
elif decision == "no":
    print(f"{player_name}, you decide to wait. Perhaps courage will find you later.")
else:
    print("Confused, you stand still, unsure of what to do")