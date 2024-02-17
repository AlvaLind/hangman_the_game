def instructions():
    """
    Prints the game Instructions 
    """
    print(f"""
--------------------
Hangman Instructions
--------------------
The objective of the game is to guess the hidden word before the hangman is 
fully drawn.

How to Play:
1. Choose a theme for the word you will be trying to guess.
2. A hidden word is chosen, and you must guess its letters one by one.
3. You have 7 incorrect guesses before the hangman is complete and you lose.
4. Each incorrect guess results in a part of the hangman being drawn.
5. Guess the letters wisely to reveal the hidden word before it's too late!

Rules:
- Each guess must be a single letter.
- Only alphabetic characters are valid guesses. Special characters and numbers 
    will not be accepted.

Good luck and have fun! Let's begin or continue your game below.
""")
