import random 

print("Welcome! The theme of this game is countries. Let's play hangman!")
print(".......................................................................")

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
display_hidden_word(pickWord)

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
        |    
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |    
        |    
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |     |
        |     
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |    /|
        |     
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |    /|\\
        |     
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |    /|\\
        |    / 
        |    
        |
        --------
        """,
        """
        +-----+
        |     |
        |     O
        |    /|\\
        |    / \\
        |    
        |
        --------
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

while incorrect_guesses < 6:
    print("\nGuessed letters: ", " ".join(all_letters_guessed))
    guessedLetter = input("Please guess a letter: ").lower()
    
    if len(guessedLetter) != 1 or not guessedLetter.isalpha():  #Check that the guessed value is a letter
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
            print("\nCongratulations! You've guessed the word:", pickWord)
            break
    else:
        incorrect_guesses += 1
        create_hangman(incorrect_guesses)
        printWord(all_letters_guessed)

if incorrect_guesses == 6:
    print("You're out of guesses! The correct country was:", pickWord)


