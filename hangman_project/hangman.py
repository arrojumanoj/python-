import random

# Show hangman ASCII art based on number of wrong guesses
def display_hangman(wrong_count):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[wrong_count])

# Load words from a file
def load_words(filename="words.txt"):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return [word.lower() for word in words if len(word) >= 4]

# Choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Main game function
def play_game():
    words = load_words()
    word = choose_word(words)      # The word to guess
    guessed_letters = []           # Letters guessed by the user
    wrong_letters = []             # Wrong guesses
    max_wrong = 6                  # Max number of wrong guesses allowed

    print("🎮 Welcome to Hangman!\n")

    while True:
        # Display current word state
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong letters:", " ".join(wrong_letters))
        print("Remaining tries:", max_wrong - len(wrong_letters))
        display_hangman(len(wrong_letters))

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter one alphabet letter only.")
            continue
        if guess in guessed_letters or guess in wrong_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Check the guess
        if guess in word:
            print("✅ Correct!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong!")
            wrong_letters.append(guess)

        # Check win
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word.upper())
            break

        # Check loss
        if len(wrong_letters) >= max_wrong:
            display_hangman(len(wrong_letters))
            print("\n💀 You lost! The word was:", word.upper())
            break

# Start the game
play_game()
