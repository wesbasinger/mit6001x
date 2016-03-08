import unittest

def flatten(aList):
    if all(not isinstance(item, list) for item in aList):
        return aList
    flat = []
    for item in aList:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)        
    return flatten(flat)
        
    
        


class TestFlatten(unittest.TestCase):
    
    def test_Test_Case_1(self):
        self.assertEqual(
            flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]),
            [1,'a','cat',2,3,'dog',4,5]
            )
 

if __name__ == '__main__':
    unittest.main()