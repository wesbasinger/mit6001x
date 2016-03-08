import unittest

def f(s):
    return 'a' in s

L = ['']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    for string in L:
        if not f(string):
            L.remove(string)
    return len(L)
    
print satisfiesF(L)
print L
#run_satisfiesF(L, satisfiesF)
        
    
        

"""
class TestSatisfiesF(unittest.TestCase):
    
    def test_Test_Case_1(self):
     
        self.assertEqual(
            output,
            1
            )
        self.assertEqual(
            L,
            ['baaab']
        )
            

if __name__ == '__main__':
    unittest.main()
"""