import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'computer']
    word = random.choice(words)  # Choose a random word
    guessed_word = ['_'] * len(word)  # List of underscores to represent the word
    attempts = 6  # Number of chances the player has
    guessed_letters = []  # To track guessed letters

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters: " + ", ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        # Check if the letter is already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        # If the letter is in the word, update the guessed_word list
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts -= 1  # Decrease the number of attempts

        # Check if the player has guessed all the letters
        if ''.join(guessed_word) == word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Run the game
hangman()
