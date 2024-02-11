
print("Welcome! The theme of this game is countries. Let's play hangman!")
print("......................................................")

gameWords = ["australia", "sweden", "finland", "norway", "denmark", "poland", "ireland", "spain", "italy", "portugal", "greece", "albania", "ukrain", "switzerland", "cyprus", "argentina", "mauritius", "canada", "united states", "mexico", "morocco", "brazil", "chile", "philippines", "new zealand", "qatar", "estonia", "france", "singapore", "germany", "guatemala", "turkey", "jordan", "syria", "japan", "china", "russia"]

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
