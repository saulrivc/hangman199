import random

word_list = ["Mango", "Strawberry", "Banana", "Pineapple", "Blueberry"]

word = random.choice(word_list)

print(word_list)

guess = input("Please enter a single letter: ")

print("You guessed:", guess)

import random

word_list = ["Mango", "Strawberry", "Banana", "Pineapple", "Blueberry"]

word = random.choice(word_list)

print(word_list)

# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Step 1: Validate input
if len(guess) == 1 and guess.isalpha():
    # Step 2: Valid input
    print("Good guess!")
else:
    # Step 3: Invalid input
    print("Oops! That is not a valid input.")

