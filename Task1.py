import random
def hangman():
    # Step 1: Word selection by randomly from list of words 
    words = ["python", "java", "hangman", "programming", "developer"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6  # Set  limit on incorrect guesses
    guessed_letters = []
    print("Welcome to Hangman Game!")
    print(" ".join(guessed_word))
    # Step 2: Main game loop
    while attempts_left > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()
        # Step 3: Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        # Step 4: Check the guessed letter is in word or not
        if guess in word_to_guess:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Wrong guess. You have {attempts_left} attempts left.")
        # Step 5: Display progress
        print(" ".join(guessed_word))
    # Step 6: End of game
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nYou ran out of attempts! The word was:", word_to_guess)
# start the game by calling hangman method
hangman()
