# Hangman in Python
import random

endGame = False
hangman = 0
maxErrors = 6
guesses = {}

def print_board():
    head = ""
    body = ""
    larm = " "
    rarm = ""
    lleg = ""
    rleg = ""
    if hangman > 0:
        head = "0"
    if hangman > 1:
        body = "|"
    if hangman > 2:
        larm = "-"
    if hangman > 3:
        rarm = "-"
    if hangman > 4:
        lleg = "/"
    if hangman > 5:
        rleg = "\\"

    print("   ___\n" + \
          "  /   |\n" + \
          " |    " + head + "\n" + \
          " |   " + larm + body + rarm + "\n" + \
          " |   " + lleg + " " + rleg + "\n" + \
          "/ \\\n")

    for letter in word:
        if letter in guesses:
            print(letter + " ", end='')
        else:
            print("_ ", end='')
    print("\n")

    print("Guesses: ", end='')
    for letter in guesses.keys():
        if letter not in word:
            print(letter + " ", end='')
    print("\n")

def dictionary_word():
    dict = "/usr/share/dict/words"
    return random.choice(open(dict).read().splitlines()).strip()

word = dictionary_word().lower()
while (not endGame):
    print_board()
    guess = input("Choose a letter or make a guess: ").lower()
    if len(guess) == 1:
        # they are guessing a letter
        if guess in guesses.keys():
            print("Silly player, you already guessed " + guess)
        else:
            guesses[guess] = 1
            if guess in word:
                print("Good guess! " + guess + " is in the word.")
            else:
                print("Sorry " + guess + " is NOT in the word.")
                hangman += 1
    else:
        # see if they guessed the word correctly
        if word == guess:
            print("Correct! " + word + " is the word.")
            endGame = True
        else:
            print("Incorrect guess")
            hangman += 1
    
    if hangman >= maxErrors:
        print_board()
        print("You lose! " + word + " was the answer.")
        endGame = True

    won = True
    for letter in word:
        if letter not in guesses:
            won = False
            break
    if won:
        print("You found all the letters in " + word + ". You win!")
        endGame = True
