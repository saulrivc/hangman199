# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the **computer thinks of a word** and the **user tries to guess it** one letter at a time.

## 📖 Description

This beginner-friendly project focuses on the **early stages of a Hangman game**, including:

- Selecting a random word from a list
- Prompting the user to input a guess
- Validating the input to ensure it's a **single alphabetical letter**
- Providing appropriate feedback

It sets the groundwork for building a fully functional Hangman game with tracking correct/incorrect guesses, number of lives, and visual display of progress.

### 💡 What I learned

- How to use the `random` module, specifically `random.choice()`
- How to take user input with `input()`
- How to perform basic input validation (`isalpha()` and `len()`)
- Structuring a Python script to separate logic clearly

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/hangman.git
   cd hangman
   ```

2. **Make sure Python is installed**:
   ```bash
   python --version
   ```

## ▶️ Usage

Run the script using Python:

```bash
python hangman.py
```

You'll see a list of possible words and be prompted to enter a single letter. The script will validate your input and respond accordingly.

## 📁 File Structure

```
hangman/
├── hangman.py        # Main game script
└── README.md         # Project documentation
```

## 🔒 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
