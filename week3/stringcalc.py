def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length = 0
    for letter in aStr:
        length += 1
    return length

import unittest

class TestL5Problem6(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(
            lenIter("string"),
            6
        )
        
 
if __name__ == '__main__':
    unittest.main()