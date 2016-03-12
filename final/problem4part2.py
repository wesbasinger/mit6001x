import unittest

def getSublists(L, n):
    sublists = []
    slice_position = 0
    while slice_position < len(L) - n + 1:
        sublists.append(L[slice_position:slice_position+n])
        slice_position += 1
    return sublists

def longestRun(L):
    for slice_length in range(len(L), 0, -1):
        all_slices = getSublists(L, slice_length)
        for test_slice in all_slices:
            if test_slice == range(test_slice[0], test_slice[slice_length-1]):
                return len(test_slice)





class TestCasesForFinalProblem4Part1(unittest.TestCase):

    def test_getSublists(self):
        self.assertEqual(
            getSublists(
                [10, 4, 6, 8, 3, 4, 5, 7, 7, 2],
                4
            ),
            [
                [10, 4, 6, 8],
                [4, 6, 8, 3],
                [6, 8, 3, 4],
                [8, 3, 4, 5],
                [3, 4, 5, 7],
                [4, 5, 7, 7],
                [5, 7, 7, 2]
            ]
        )
        self.assertEqual(
            getSublists(
                [1, 1, 1, 1, 4],
                2
            ),
            [[1, 1], [1, 1], [1, 1], [1, 4]]
        )
    def test_longestRun(self):
        self.assertEqual(
            longestRun(
                [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
            ),
            5
        )

if __name__ == '__main__':
    unittest.main()
