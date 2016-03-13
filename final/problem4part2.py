import unittest

def getSublists(L, n):
    sublists = []
    slice_position = 0
    while slice_position < len(L) - n + 1:
        sublists.append(L[slice_position:slice_position+n])
        slice_position += 1
    return sublists

def longestRun(L):
    longestRun = 1
    all_lists = []
    for i in range(1, len(L)):
        all_lists.extend(getSublists(L, i))
    for subset in all_lists:
        current_run = 1
        for i in range(len(subset)):
            try:
                if subset[i + 1] >= subset[i]:
                    current_run +=1
                else:
                    current_run = 1
            except IndexError:
                break
        if current_run > longestRun:
            longestRun = current_run
    return longestRun


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
        self.assertEqual(
            longestRun([0]), 1
        )
        self.assertEqual(longestRun([1,1,1,1,1]), 5)

        self.assertEqual(longestRun([-10, -5, 0, 5, 10]),
            2
        )
        self.assertEqual(longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]), 5)

        self.assertEqual(longestRun([1, 2, 3, -1, -2, -3, -4, -5, -6]), 3)

        self.assertEqual(longestRun([-1, -2, -3, -4, -5, -6, -7, 2, 3]), 3)

        self.assertEqual(longestRun([1, 3, 5, -1, -3, -5, -7, 1, 3, 5])
, 4)
        self.assertEqual(longestRun([10, 8, 9, 5, 6, 7, 1, 2, 3, 4]),4)

        self.assertEqual(longestRun([14, 16, 18, 20, 8, 10, 12, 4, 6, 2]), 4)

        self.assertEqual(longestRun([7, 4, 1, -7, -11]), 1)

        self.assertEqual(longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9])
, 6)
        self.assertEqual(longestRun([1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]), 5)





if __name__ == '__main__':
    unittest.main()
