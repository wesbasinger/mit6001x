balance = 4213
annualInterestRate = 0.20
monthlyPaymentRate = 0.04

def print_info():
    current_balance = balance
    total_paid = 0
    for month in range(1,13):
        print "Month: %s" % month
        min_payment = current_balance*monthlyPaymentRate
        total_paid += min_payment
        print "Minimum monthly payment: %s" % round(min_payment,2)
        remaining = (current_balance - min_payment)*(annualInterestRate/12+1)
        current_balance = remaining
        print "Remaining balance: %s" % round(current_balance,2)
    print "Total paid: %s" % round(total_paid,2)
    print "Remaining balance: %s" % round(current_balance, 2)

print_info()