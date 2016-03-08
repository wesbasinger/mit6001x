
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
satisfied = False
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1+ monthlyInterestRate)**12)/ 12.0


def makeMonthlyPayments(guess, balance):
    for month in range(1,13):
        balance -= guess
        balance *= 1 + monthlyInterestRate
    return balance
    
def makeGuess(monthlyPaymentLowerBound, monthlyPaymentUpperBound):
    return (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2 
        
while not satisfied:
    guess = makeGuess(monthlyPaymentLowerBound, monthlyPaymentUpperBound)
    effectiveBalance = makeMonthlyPayments(guess, balance)
    if effectiveBalance < -0.0001:
        monthlyPaymentUpperBound = guess
    elif effectiveBalance > 0.0001:
        monthlyPaymentLowerBound = guess
    else:
        satisfied = True
        print "Lowest Payment: %s" % guess
        
    
    


#
#
#
#guess = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
#satisfied = False
#
#def makeMonthlyPayments(guess, balance):
#    for month in range(1,13):
#        balance -= guess
#        balance *= 1 + monthlyInterestRate
#    return balance
#
#def calculate(balance, annualInterestRate):
#
#    for i in range(4):
#        print "%s: lower:%s upper:%s" %(i, monthlyPaymentLowerBound, monthlyPaymentUpperBound)
#        newBalance = makeMonthlyPayments(guess, balance)
#        if newBalance < -0.001:
#            print "bal neg"
#            monthlyPaymentUpperBound = guess
#            print "guess is new upper"
#        elif newBalance > 0.001:
#            print "bal pos"
#            monthlyPaymentLowerBound = guess
#            print "guess is new lower"
#        else:
#            satisfied = True
#            print guess
            


#calculate(balance, annualInterestRate)
            


        
                
            
        
        




import unittest

class TestProblemSet2Problem2(unittest.TestCase):
    
    def test_Test_Case_1(self):
        self.assertEqual(calculate(320000, 0.2), 29157.09)
        
    def test_Test_Case_2(self):
        self.assertEqual(calculate(999999, 0.18), 90325.03)

if __name__ == '__main__':
    unittest.main()