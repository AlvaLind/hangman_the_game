import random 
import os

def clear_terminal():
    os.system('clear')


def get_player_name():
    """Asks the player to input their name."""
    while True:
        player_name = input("Please enter player name: \n").strip()
        if player_name and len(player_name) <= 15:
            return player_name
        elif not player_name:
            print("Name can not be empty")
        else:
            print("Name can not be longer than 15 characters")


def select_theme():
    """Asks the player to select a theme."""
    print(
        f"""
    Select a game theme: 
    ..........................
    1. Countries
    2. Cities
    3. Sports
    ..........................
        """
    )
    while True:
        theme_choice = input(
            "Please enter the number of your chosen theme:\n"
            ).strip()
        if theme_choice in ["1", "2", "3"]:
            return theme_choice
        elif theme_choice == "!":
            instructions()
        else:
            print(
                f"""
{theme_choice} is not a valid choice. 
Please enter a number between 1 and 3 or enter '!' for instructions.
                """
            )


def get_word(theme_choice):
    """
    Returns a randomly selected word based on the chosen theme.
    """
    if theme_choice == "1":
        theme_words = ["australia", "sweden", "finland", "norway", "denmark", "poland", "ireland", "spain", "italy", "madagascar", "fiji", "portugal", "greece", "albania", "ukrain", "switzerland", "cyprus", "argentina", "mauritius", "canada", "united states", "mexico", "morocco", "brazil", "chile", "philippines", "new zealand", "qatar", "estonia", "france", "singapore", "germany", "guatemala", "turkey", "jordan", "syria", "japan", "china", "russia"]
        theme = "countries"
    elif theme_choice == "2":
        theme_words = ["london", "paris", "stockholm", "melbourne", "tokyo", "new york", "rome", "sydney", "beijing", "moscow", "cairo", "berlin", "amsterdam", "istanbul", "mumbai", "rio de janeiro", "dubai", "los angeles", "athens", "toronto", "singapore", "barcelona", "helsinki", "oslo"]
        theme = "cities"
    elif theme_choice == "3":
        theme_words = ["football", "basketball", "tennis", "soccer", "baseball", "volleyball", "golf", "rugby", "cricket", "hockey", "swimming", "cycling", "boxing", "skiing", "surfing", "running", "wrestling", "badminton", "table tennis", "rowing"]
        theme = "sports"
    return random.choice(theme_words), theme   

def instructions():
    """
    Prints the game Instructions 
    """
    print("--------------------")
    print("Hangman Instructions")
    print("--------------------")
    print("Guess the letters to reveal the hidden country before the man gets hanged.")
    print("You can guess as many times as you want but you only have 7 incorrect guesses")
    print("until you loose. So use your guesses carefully!")
    print("Each guess must only be a single letter.")
    print("Good luck! Begin or continue your game below.")
    print("--------------------")

def display_hidden_word(pickWord):
    """
    Creates an underscore for every letter and a space for the spaces between words where required.
    """
    for x in pickWord:
        if x == ' ':
            print(" ", end=" ")
        else:
            print("_", end=" ")

def create_hangman(incorrect):
    """create hangman when incorrect answer"""
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

    One more incorrect guess 
    and you're out of lives!
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

def printWord(guesses, pickWord):
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


print("Welcome to Hangman The Game!")
print(" ")

player_name = get_player_name()

print(" ")
print("Hello", player_name, end = "! ")
print("\nEnter '!' at anytime for intructions.")


def play_hangman(pickWord):
    """Function to play the game."""
    print("Your word is: ", end=" ")
    display_hidden_word(pickWord)
    print(" ")

    length_of_word = len(pickWord.replace(" ", ""))   #Remove any spaces from pickWord and then calculate the number of letters
    incorrect_guesses = 0 
    letter_occurances = 0
    all_letters_guessed = []

    while incorrect_guesses < 7:
        print("\nGuessed letters: ", " ".join(all_letters_guessed))
        guessedLetter = input("Please guess a letter: \n").strip().lower()
        
        if guessedLetter == '!':
            instructions()
            create_hangman(incorrect_guesses)
            correct_letters = printWord(all_letters_guessed, pickWord)
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
            correct_letters = printWord(all_letters_guessed, pickWord)
            
            if correct_letters == length_of_word:
                print("\nCongratulations", player_name, end = "! ")
                print("You've guessed correctly, the word was:", pickWord)
                break
        else:
            incorrect_guesses += 1
            create_hangman(incorrect_guesses)
            printWord(all_letters_guessed, pickWord)

    if incorrect_guesses == 7:
        print("\nOH NO", player_name, end = "! ")
        print("You're out of guesses \nThe correct word was:", pickWord)

while True:
    theme_choice = select_theme()
    pickWord, theme = get_word(theme_choice)
    clear_terminal()
    print(
        f"""
The theme of this game is {theme}

Let's play hangman!
...........................................................
        """
        )
    play_hangman(pickWord)
    while True:
        play_again = input(
            "\nDo you want to play again? Enter yes/y or no/n: \n"
            ).strip().lower()
        print(" ")
        if play_again == "yes" or play_again == "y":
            clear_terminal()
            break
        elif play_again == "no" or play_again == "n":
            clear_terminal()
            print(
                "No problem, thank you for playing! Hope to see you again soon"
            )
            exit()
        else:
            print(
                f"""
{play_again} is not a valid input. Please enter 'yes/y' or 'no/n'.
                """
                )
