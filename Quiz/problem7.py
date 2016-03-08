import unittest

def f(a, b):
    return a > b

def dict_interdiff(d1, d2):
    intersect_dict = {}
    for key in d1:
        if key in d2:
            intersect_dict[key] = f(d1[key], d2[key])
    diff_dict = {}
    for key in d1:
        if key not in d2:
            diff_dict[key] = d1[key]
    for key in d2:
        if key not in d1:
            diff_dict[key] = d2[key]
    return (intersect_dict, diff_dict)
        
    
        


class TestDictInterdiff(unittest.TestCase):
    
    def test_Test_Case_1(self):
        """
        if f(a, b) returns a + b
        """
        self.assertEqual(
            dict_interdiff(
                {1:30, 2:20, 3:30, 5:80},
                {1:40, 2:50, 3:60, 4:70, 6:90}
            ),
            ({1: 70, 2: 70, 3: 90},{4: 70, 5: 80, 6: 90})
            )
            
    def test_Test_Case_2(self):
        """
        If f(a, b) returns a > b
        """
        self.assertEqual(
            dict_interdiff(
                {1:30, 2:20, 3:30},
                {1:40, 2:50, 3:60}
            ),
            ({1: False, 2: False, 3: False},{})
            )
 

if __name__ == '__main__':
    unittest.main()