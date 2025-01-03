import random
def hangman(level):
    # Step 1: Word selection
    if level==1:
        words = ["python","java","software","programming","developer","computer","testing","coding","laptop","debug"]
        attempts_left = 6
    if level==2:
        words=["function","class", "integer", "network","firewall", "compiler", "debugger", "program", "gateway", "datamart", "bandwidth", "recursion"]
        attempts_left = 4
    if level==3:
        words=["encryption", "polymorphism", "cybersecurity","normalization", "datawarehouse", "cryptography","distributed", "asynchronous", "virtualization","multithreading", "objectoriented", "inheritance"]
        attempts_left = 3
    word_to_guess = random.choice(words)
    guessed_word=["_"]*len(word_to_guess)
    guessed_letters=[]
    print(f"Welcome to Hangman level {level}!")
    print(" ".join(guessed_word))
    # Step 2:Main game loop
    while attempts_left>0 and "_" in guessed_word:
        guess=input("\nGuess a letter: ").lower()
        #Step 3: Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        # Step 4: Check the guess
        if guess in word_to_guess:
            print(f"Good job! {guess} is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter==guess:
                    guessed_word[i]=guess
        else:
            attempts_left-=1
            print(f"Wrong guess. You have {attempts_left} attempts left.")
        # Step 5: Display progress
        print(" ".join(guessed_word))
    # Step 6: End of game
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:",word_to_guess)
        level+=1
        return level
    else:
        print("\nYou ran out of attempts! The word was:",word_to_guess)
        level=0
        return level
#Run the game
def start():
    level=1
    while level>0:
        level=hangman(level)
        
        if(level>3):
            break
    if(level>3):
        print("Excellent you are genius. you have passed all the levels of Hangman Game.!")
        press=int(input('press 1 to play again.!'))
        if(press==1):
            start()
    else:
        press=int(input('press 1 to play again.!'))
        if(press==1):
            start()
start()
