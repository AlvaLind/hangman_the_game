import random 

def get_player_name():
    """
    Asks the player to input their name.
    """
    player_name = input("Please enter player name:")
    return player_name

player_name = get_player_name()

print(" ")
print("Welcome", player_name, end = "! ")
print("The theme of this game is countries. Let's play hangman!")
print("Begin the game below or enter 1 at any time for instructions.")
print(".......................................................................")
print(" ")


def instructions():
    """
    Prints the game Instructions 
    """
    print("--------------------")
    print("Hangman Instructions")
    print("--------------------")
    print("Guess the letters to reveal the hidden country before the man gets hanged.")
    print("You can guess as many times as you want but you only have 7 incorrect guesses until you loose. So use your guesses carefully!")
    print("Each guess must only be a single letter.")
    print("Good luck! Begin or continue your game below.")

gameWords = ["australia", "sweden", "finland", "norway", "denmark", "poland", "ireland", "spain", "italy", "madagascar", "fiji", "portugal", "greece", "albania", "ukrain", "switzerland", "cyprus", "argentina", "mauritius", "canada", "united states", "mexico", "morocco", "brazil", "chile", "philippines", "new zealand", "qatar", "estonia", "france", "singapore", "germany", "guatemala", "turkey", "jordan", "syria", "japan", "china", "russia"]

def display_hidden_word(pickWord):
    """
    Creates an underscore for every letter and a space for the spaces between words where required.
    """
    for x in pickWord:
        if x == ' ':
            print(" ", end=" ")
        else:
            print("_", end=" ")

pickWord = random.choice(gameWords)
pickWord = pickWord.lower() # convert to lowercase to make case-insensitive
print("Your word is: ", end=" ")
display_hidden_word(pickWord)
print(" ")

def create_hangman(incorrect):
    """
    create hangman when incorrect answer
    """
    stages = [
        """
        +-----+
        |     |
        |     
        |      
        |    ___
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |     O
        |      
        |    ___
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |     O
        |     |
        |    ___
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |    \\O
        |     | 
        |    ___
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |    \\O/
        |     |
        |    ___
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |    \\O/
        |     |
        |    /__
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |    \\O/
        |     |
        |    /_\\
        |   |   |
        |___|___|_____
        """,
        """
        +-----+
        |     |
        |     |
        |     O
        |    /|\\
        |    / \\    
        |_____________
        """
    ]
    print(stages[incorrect])

def printWord(guesses):
    """
    Takes list of all letters guessed so far and checks if they are in the hidden word. 
    Prints result to the terminal, and returns number of correct letters in the word. 
    """
    correctLetters = 0
    for char in pickWord:
        if char == ' ':
            print(" ", end=" ")
        elif char in guesses:
            print(char, end=" ")
            correctLetters += 1
        else:
            print("_", end=" ")
    print(" ")
    return correctLetters 

length_of_word = len(pickWord.replace(" ", ""))   #Remove any spaces from pickWord and then calculate the number of letters
incorrect_guesses = 0 
letter_occurances = 0
all_letters_guessed = []

while incorrect_guesses < 7:
    print("\nGuessed letters: ", " ".join(all_letters_guessed))
    guessedLetter = input("Please guess a letter: ").lower()
    
    if guessedLetter == '1':
        instructions()
        create_hangman(incorrect_guesses)
        correct_letters = printWord(all_letters_guessed)
        continue

    if len(guessedLetter) != 1 or not guessedLetter.isalpha():  #Check that the guessed value is a single letter
        print("Please enter a valid letter.")
        continue
    
    if guessedLetter in all_letters_guessed:
        print("You have already guessed that letter.")  #Check that the guess is a new letter
        continue
    
    all_letters_guessed.append(guessedLetter)

    if guessedLetter in pickWord:
        letter_occurances += pickWord.count(guessedLetter)
        create_hangman(incorrect_guesses)
        correct_letters = printWord(all_letters_guessed)
        
        if correct_letters == length_of_word:
            print("\nCongratulations", player_name, end = "! ")
            print("You've guessed correctly, the word was:", pickWord)
            break
    else:
        incorrect_guesses += 1
        create_hangman(incorrect_guesses)
        printWord(all_letters_guessed)

if incorrect_guesses == 7:
    print("OH NO", player_name, end = "! ")
    print("You're out of guesses :( \nThe correct country was:", pickWord)


