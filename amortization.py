class Amoritzation:

    def monthly_payment(principal, interest_rate, period):
        i = interest_rate / 1200
        j = (1+i) ** (period * 12)
        x = (principal * i *j) / (j-1)
        return x

    def amortization_schedule(principal, interest_rate, period):
        amort_table={}
        monthly_pay = monthly_payment(principal, interest_rate, period)
        i = interest_rate / 1200
        number = 1
        balance = principal
        while number <= period * 12:
            interest = balance * i
            principal_paid = monthly_pay - interest
            balance = balance - principal_paid
            amort_table[number] = [round(monthly_pay,2),round(interest,2),round(principal_paid,2),round(balance,2)]
            #print("Payment = " + str(monthly_pay) + " Int = " + str(interest) + " Prin = " + str(principal_paid) + " Balance = " + str(balance))
            number += 1
        return amort_table