def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    pass
    outputList = []
    for letter in secretWord:
        if letter in lettersGuessed:
            outputList.append(letter)
        else:
            outputList.append('_')
    return ''.join(outputList)
            


import unittest

class TestProblemSet3HangmanPrintGuess(unittest.TestCase):
    
    def test_isGuessPrinted(self):
        secretWord = 'apple'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(getGuessedWord(secretWord, lettersGuessed), '_pp_e')
        
if __name__ == '__main__':
    unittest.main()