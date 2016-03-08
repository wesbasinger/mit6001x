import unittest

def sum_pairwise_products(listA, listB):
    dot_product = 0
    for i in range(len(listA)):
        dot_product += listA[i]*listB[i]
    return dot_product
        










class TestPairWiseProducts(unittest.TestCase):
    
    def test_Test_Case_1(self):
        self.assertEqual(
            sum_pairwise_products(
                [1, 2, 3],
                [4, 5, 6]
            ),
            32
            )
 

if __name__ == '__main__':
    unittest.main()