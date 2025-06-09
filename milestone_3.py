secret_word = "apple"  # The secret word to guess

def is_guess_in_word_and_print_message(user_guess):
    """Check if the guessed letter is in the secret word and print the result."""
    user_guess = user_guess.lower()
    if user_guess in secret_word:
        print(f"Good guess! '{user_guess}' is in the word.")
    else:
        print(f"Sorry, '{user_guess}' is not in the word. Try again.")

def prompt_user_for_single_letter_guess():
    """Prompt the user repeatedly until they provide a valid single alphabetical letter."""
    while True:
        user_guess = input("Please enter a single letter: ")
        if len(user_guess) == 1 and user_guess.isalpha():
            return user_guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def play_guessing_round():
    """Perform one round of guessing: prompt for input and check the guess."""
    user_guess = prompt_user_for_single_letter_guess()
    is_guess_in_word_and_print_message(user_guess)

# Run the game for one round
play_guessing_round()
