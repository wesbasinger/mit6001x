def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    print "start:%s stop%s step:%s" % (start, stop, step)
    numberOfRectangles = (stop - start) / step
    print "numberofrectangles:%s" % numberOfRectangles
    
    base = step
    print "base:%s" % base
    inc = []
    for i in range(int(numberOfRectangles)):
        inc.append(start + step*i)
    print inc
    totalArea = 0.0
    for iv in inc:
        totalArea += step*f(iv)
    return totalArea




import unittest

class TestProblemSet3RadiationExposure(unittest.TestCase):
    
    def test_case_1(self):
        self.assertAlmostEqual(
            radiationExposure(0,5,1),
            39.10318784326239
        )
        
    def test_case_2(self):
        self.assertAlmostEqual(
            radiationExposure(5,11,1),
            22.94241041057671
        )
        
    def test_case_3(self):
        self.assertAlmostEqual(
            radiationExposure(0,11,1),
            62.0455982538
        )
    def test_case_4(self):
        self.assertAlmostEqual(
            radiationExposure(40, 100, 1.5),
            0.434612356115
        )
 
if __name__ == '__main__':
    unittest.main()