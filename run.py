import random
import os
import sys
import instructions
import countries
import cities
import sports


def clear_terminal():
    #os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player_name():
    """Asks the player to input their name."""
    while True:
        player_name = input(
            f"""
Please enter player name:
(Must contain at least one letter and cannot include special characters)
""").strip()
        if not player_name:
            clear_terminal()
            print("Name cannot be empty")
        elif len(player_name) > 15:
            clear_terminal()
            print("Name cannot be longer than 15 characters")
        elif not any(char.isalpha() for char in player_name.replace(' ', '')):
            clear_terminal()
            print("Name must contain at least one letter")
        elif not all(char.isalnum() or char.isspace() for char in player_name):
            clear_terminal()
            print("Name cannot contain special characters")
        else:
            return player_name


def select_theme():
    """Asks the player to select a theme."""
    while True:
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
        theme_choice = input(
            "Please enter the number of your chosen theme:\n").strip()
        if not theme_choice:
            clear_terminal()
            print(
                f"""
Choice cannot be empty, please enter a number between 1 and 3 or
enter '!' for instructions.""")
            continue

        if theme_choice in ["1", "2", "3"]:
            return theme_choice
        elif theme_choice == "!":
            clear_terminal()
            instructions.instructions()
        else:
            if len(theme_choice) != 1:
                clear_terminal()
                print(
                    f"""
{theme_choice} has too many characters, please enter only one number
between 1 and 3 or enter '!' for instructions.
                    """)
            else:
                clear_terminal()
                print(
                    f"""
{theme_choice} is not a valid choice, please enter a number between 1 and 3 or
enter '!' for instructions.
                """
                )


def get_word(theme_choice):
    """
    Returns a randomly selected word based on the chosen theme.
    """
    if theme_choice == "1":
        theme_words = countries.get_countries_words()
        theme = "countries"
    elif theme_choice == "2":
        theme_words = cities.get_cities_words()
        theme = "cities"
    elif theme_choice == "3":
        theme_words = sports.get_sports_words()
        theme = "sports"
    return random.choice(theme_words), theme


def display_hidden_word(pick_word):
    """
    Creates an underscore for every letter and a space for the spaces between
    words where required.
    """
    for x in pick_word:
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


def printWord(guesses, pick_word):
    """
    Takes list of all letters guessed so far and checks if they are in the
    hidden word. Prints result to the terminal, and returns number of correct
    letters in the word.
    """
    correctLetters = 0
    for char in pick_word:
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
player_name = get_player_name()
print("\nHello", player_name, end="!")
print("\nIf you're feeling lost you can enter '!' at anytime for intructions.")


def play_hangman(pick_word):
    """Function to play the game."""
    try:
        create_hangman(0)
        print("Your word is: ", end=" ")
        display_hidden_word(pick_word)
        print(" ")

        length_of_word = len(pick_word.replace(" ", ""))
        incorrect_guesses = 0
        letter_occurances = 0
        all_letters_guessed = []

        while incorrect_guesses < 7:
            print("\nGuessed letters: ", " ".join(all_letters_guessed))
            guessedLetter = input("Please guess a letter: \n").strip().lower()

            if not guessedLetter:
                clear_terminal()
                create_hangman(incorrect_guesses)
                correct_letters = printWord(all_letters_guessed, pick_word)
                print(
                    f"""
Guess cannot be empty. Please enter a letter.""")
                continue

            if guessedLetter == '!':
                clear_terminal()
                instructions.instructions()
                create_hangman(incorrect_guesses)
                correct_letters = printWord(all_letters_guessed, pick_word)
                continue

            if len(guessedLetter) != 1 or not guessedLetter.isalpha():
                if len(guessedLetter) != 1:
                    clear_terminal()
                    create_hangman(incorrect_guesses)
                    correct_letters = printWord(all_letters_guessed, pick_word)
                    print(
                        f"""
{guessedLetter} has too many characters, please enter only one character.""")
                elif guessedLetter.isdigit():
                    clear_terminal()
                    create_hangman(incorrect_guesses)
                    correct_letters = printWord(all_letters_guessed, pick_word)
                    print(f"""
{guessedLetter} is a number. Please enter a letter.""")
                else:
                    clear_terminal()
                    create_hangman(incorrect_guesses)
                    correct_letters = printWord(all_letters_guessed, pick_word)
                    print(
                        f"""
{guessedLetter} is not a letter. Please enter a letter.""")
                continue

            if guessedLetter in all_letters_guessed:
                clear_terminal()
                create_hangman(incorrect_guesses)
                correct_letters = printWord(all_letters_guessed, pick_word)
                print(
                    f"""
You have already guessed {guessedLetter}, please guess another letter.""")
                continue

            all_letters_guessed.append(guessedLetter)

            if guessedLetter in pick_word:
                clear_terminal()
                letter_occurances += pick_word.count(guessedLetter)
                create_hangman(incorrect_guesses)

                correct_letters = printWord(all_letters_guessed, pick_word)

                if correct_letters < length_of_word:
                    print("\nYou guessed correctly. Keep it up!")

                elif correct_letters == length_of_word:
                    print("\nCongratulations", player_name, end="! ")
                    print("You've guessed correctly, the word was:", pick_word)
                    break
            else:
                clear_terminal()
                incorrect_guesses += 1
                create_hangman(incorrect_guesses)
                if incorrect_guesses == 6:
                    printWord(all_letters_guessed, pick_word)
                    print(
                        "\nOne more incorrect guess and you're out of lives!"
                        )
                elif incorrect_guesses == 7:
                    print("\nOH NO", player_name, end=", ")
                    print(
                        f"""
You're out of guesses! \nThe correct word was:""", pick_word)
                else:
                    printWord(all_letters_guessed, pick_word)
                    print("\nOops, incorrect guess. Keep guessing")
    except KeyboardInterrupt:
        clear_terminal()
        print("\nGame interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print("Unfortunately an error occurred:", e)
        sys.exit(1)


def main():
    while True:
        theme_choice = select_theme()
        pick_word, theme = get_word(theme_choice)
        clear_terminal()
        print(f"""
The theme of this game is {theme}
\nLet's play hangman!\n
        """)
        play_hangman(pick_word)
        if not play_again():
            clear_terminal()
            print(
                f"""
No problem, thank you for playing! Hope to see you again soon :)""")
            break


def play_again():
    """Ask the user if they want to play again."""
    while True:
        response = input(
            f"""
\nDo you want to play again? (yes/y to play agian or no/n to leave the game):\n
""").strip().lower()
        if not response:
            clear_terminal()
            print("Response cannot be empty. Please enter yes/y or no/n.")
            continue

        if response == '!':
            clear_terminal()
            instructions.instructions()
            continue
        elif response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            clear_terminal()
            print(
                f"""
{response} is not a valid input. Please enter 'yes/y' or 'no/n'.""")


if __name__ == "__main__":
    main()
