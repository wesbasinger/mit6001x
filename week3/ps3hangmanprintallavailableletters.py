import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lettersOfSecretWord = set(list(secretWord))
    if set(lettersOfSecretWord) < set(lettersGuessed):
        return True
    else:
        return False
        
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        allLetters.remove(letter)
            
    return ''.join(allLetters)
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    outputList = []
    for letter in secretWord:
        if letter in lettersGuessed:
            outputList.append(letter)
        else:
            outputList.append('_')
    return ' '.join(outputList)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    LINEBREAK = "-------------"
    
    print "Welcome to the game, Hangman!"
    
    secretWordLength = len(secretWord)
    
    print "I am thinking of a word that is %s letters long." % secretWordLength
    print LINEBREAK
    
    guessesLeft = 8
    availableLetters = string.ascii_lowercase
    lettersGuessed = []
    
    while guessesLeft > 0:
        print "You have %s guesses left." % guessesLeft
        print "Available letters: " + availableLetters
        currentGuess = raw_input('Please guess a letter: ')
        currentGuessLower = currentGuess.lower()
        if currentGuessLower in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed)
            print LINEBREAK
        else: #bad or good guess
            lettersGuessed.append(currentGuessLower)
            if isWordGuessed(secretWord, lettersGuessed):
                print "Good guess: %s" % getGuessedWord(secretWord, lettersGuessed)
                print LINEBREAK
                print "Congratulations, you won!"
                break
            if currentGuessLower in list(secretWord):
                print "Good guess: %s" % getGuessedWord(secretWord, lettersGuessed)
                print LINEBREAK

                availableLetters = getAvailableLetters(lettersGuessed)
            else:
                guessesLeft -=1
                print "Oops! That letter is not in my word: %s" %getGuessedWord(secretWord, lettersGuessed)
                availableLetters = getAvailableLetters(lettersGuessed)
                print LINEBREAK
        if guessesLeft == 0:
            print "Sorry, you ran out of guesses. The word was %s." % secretWord
        

    

            
        
        
        
        
    
    

hangman('c')
