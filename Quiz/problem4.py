import unittest

def isPalindrome(aString):
    aStringLen = len(aString)
    forward = []
    backward = []
    for letter in aString:
        forward.append(letter)
    for letter in range(1, aStringLen+1):
        backward.append(forward[letter*-1])
    if forward == backward:
        return True
    else:
        return False










class TestPalindromeFunction(unittest.TestCase):
    
    def test_Test_Case_1(self):
        self.assertEqual(
            isPalindrome("racecar"),
            True
            )
    def test_Test_Case_2(self):
        self.assertEqual(
            isPalindrome("trucker"),
            False
            )
    def test_Test_Case_2(self):
        self.assertEqual(
            isPalindrome("anna"),
            True
            )
    def test_Test_Case_2(self):
        self.assertEqual(
            isPalindrome("boob"),
            True
            )
    def test_Test_Case_2(self):
        self.assertEqual(
            isPalindrome("cammac"),
            True
            )
 

if __name__ == '__main__':
    unittest.main()