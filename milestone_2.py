import random

def create_word_list():
    """Returns a list of predefined fruit names."""
    return ["Mango", "Strawberry", "Banana", "Pineapple", "Blueberry"]

def select_random_word(word_list):
    """Selects and returns a random word from the provided list."""
    return random.choice(word_list)

def get_user_guess():
    """Prompts the user to enter a single letter and returns it."""
    return input("Please enter a single letter: ")

def is_valid_guess(guess):
    """Checks if the guess is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()

def main():
    words = create_word_list()
    selected_word = select_random_word(words)

    print("Word list:", words)

    user_guess = get_user_guess()
    print("You guessed:", user_guess)

    if is_valid_guess(user_guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()
