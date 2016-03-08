balance = 3329
annualInterestRate = 0.2

def calculate(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lowestPayment = 10
    currentBalance = balance
    
    def makeMonthlyPayments(currentBalance, lowestPayment):
        for month in range(1,13):
            currentBalance -= lowestPayment
            currentBalance *= 1 + monthlyInterestRate
        return currentBalance
    
    while currentBalance > 0:
        makeMonthlyPayments(currentBalance, lowestPayment)
        if makeMonthlyPayments(currentBalance, lowestPayment) > 0:
            lowestPayment +=01
        else:
            currentBalance = 0
            
    print "Lowest Payment: " + str(lowestPayment)

            




     
calculate(balance, annualInterestRate)
            


        
                
            
        
        




import unittest

class TestProblemSet2Problem2(unittest.TestCase):
    
    def test_Test_Case_1(self):
        self.assertEqual(calculate(3329, 0.2), 310)
        
    def test_Test_Case_2(self):
        self.assertEqual(calculate(4773, 0.2), 440)
        
    def test_Test_Case_3(self):
        self.assertEqual(calculate(3926, 0.2), 360)

if __name__ == '__main__':
    unittest.main()