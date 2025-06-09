word = "apple"  # Example secret word, can be replaced with your actual secret word

def check_guess(guess):
    guess = guess.lower()  # Step 2: convert guess to lowercase
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            # Valid input, break loop
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    # Step 3: call check_guess with the valid guess
    check_guess(guess)

# Step 4: call ask_for_input to run the code
ask_for_input()
