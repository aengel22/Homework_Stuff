import random #allows for a random word to be chose from word_list
import time ##seeds r number gen
##from word_list import word_list ##pulls word list from word_list.txt
from words import word_list
##Starts the get word function

def get_word():
    random.seed(time.time()) ##seed r number gen
    word = random.choice(word_list)
    return word.upper() #converts all letters to uppercase 

## Completes the get word function

##Starts the play function
def play(word):
    playAgain = 'Y'
    guessedRightCount = 0
    guessedWrongCount = 0
    while playAgain.upper() == 'Y':
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters: ## did user already guess that letter
                    print("You already guessed the letter", guess)
                elif guess not in word: ## letter is not in the word
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                else: ## letter is in the word
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess) ## append the guessed letter to guessed_letters
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words: ## user already guessed the word
                    print("You already guessed the word", guess)
                elif guess != word: ## user guessed the wrong word
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else: ## user guessed the correct word
                    guessed = True
                    word_completion = word
            else: ## invalid guess
                print("Not a valid guess.")
            print(display_hangman(tries)) ## print the current status of the hangman
            print(word_completion)
            print("\n")
        if guessed: ## user guessed the correct word
            print("Congrats, you guessed the word! You win!")
            guessedRightCount += 1 ## increase counter for wins
        else: ## user ran out of tries and loses
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
            guessedWrongCount += 1 ## increase counter for losses
        playAgain = input('Do you want to play again (y/n): ') ## ask to play again
        word = get_word() ## generate new word
    return (guessedRightCount,guessedWrongCount) ## return wins and losses
# #Ends the play function

##Starts the display hangman function

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
##Ends display hangman function


#Starts the main function

def main():
    guessedRight = 0
    guessedWrong = 0
    totalGuesses = 0
    averageLoss = 0
    averageWin = 0
    word = get_word()
    
    guessedRight,guessedWrong = play(word)
    totalGuesses = guessedRight + guessedWrong #gets total guesses
    averageLoss = float(guessedWrong / totalGuesses) ##avg win w/ float
    averageWin = float(guessedRight / totalGuesses) #avg loss w/ float

    print('Total games played: {0:d}'.format(totalGuesses)) #Print total games
    print('Total games won: {0:d}'.format(guessedRight)) #Print total win
    print('Average wins: {0:.2f}'.format(averageWin)) #Print avg wins
    print('Total games lost: {0:d}'.format(guessedWrong)) #Print total lost games
    print('Average lost: {0:.2f}'.format(averageLoss)) #Print avg losses
    print('\n')
    #play(word)
    #while input("Play Again? (Y/N)").upper() == "Y":
    #    word = get_word()
    #    play(word)

main()

if __name__ == "_main_":
    main()