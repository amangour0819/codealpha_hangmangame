"""
Hangman Game (Console Version)

Scope:
- 5 predefined words
- Max 6 incorrect guesses
- Basic console input/output

Key concepts used: random, while loop, if-else, strings, lists
"""

import random

WORD_LIST = ["python", "banana", "hangman", "college", "keyboard"]
MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    -------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    -------
    """,
]


def choose_word() -> str:
    """Randomly pick a word from the predefined list."""
    return random.choice(WORD_LIST)


def display_word(word: str, guessed_letters: list) -> str:
    """Return the word with unguessed letters replaced by underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("       WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} wrong guesses allowed.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_guesses}")
        if guessed_letters:
            print("Guessed so far: " + ", ".join(sorted(guessed_letters)))

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"Word: {' '.join(word)}")
            print(f"\n🎉 You won! The word was '{word}'.")
            return

    # Player ran out of attempts
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\n💀 Game over! You've run out of guesses. The word was '{word}'.")


def main():
    play_hangman()

    while True:
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again == "y":
            print("\n")
            play_hangman()
        elif again == "n":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
