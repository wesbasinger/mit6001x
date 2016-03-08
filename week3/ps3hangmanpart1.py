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
    


import unittest

class TestProblemSet3HangmanPart1(unittest.TestCase):
    
    def test_isWordGuessed(self):
        secretWord = 'apple'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual(isWordGuessed(secretWord, lettersGuessed), False)
        
    def test_isWordGuessed(self):
        secretWord = 'banana'
        lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','b','a','n']
        self.assertEqual(isWordGuessed(secretWord, lettersGuessed), True)


if __name__ == '__main__':
    unittest.main()