
import math

def interest():
    return float(input("Enter the credit interest: ")) / (12 * 100)

def n_of_payments():
    P = float(input("Enter the credit principal: "))
    A = float(input("Enter the monthly payment: "))
    i = interest()
    return math.log(A / (A - i * P), 1 + i)

def credit_principal():
    A = float(input("Enter the monthly payment: "))
    n = float(input("Enter the count of periods: "))
    i = interest()
    return A / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))

def annuity_payment():
    P = float(input("Enter the credit principal: "))
    n = float(input("Enter the number of periods: "))
    i = interest()
    return P * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))

    
calc_type = input("""What do you want to calculate?
type "n" for the number of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:
""")

if calc_type == "n":
    months = math.ceil(n_of_payments())
    years = 0
    if months == 12:
        print("You need 1 year to repay this credit!")
    elif months > 12:
        years = months // 12
        months = months % 12
        if months == 1:
            print(f"You need {years} years and 1 month to repay this credit!")
        else:
            print(f"You need {years} years and {months} months to repay this credit!")
    else:
        if months == 1:
            print(f"You need 1 months to repay this credit!")
        else:
            print(f"You need {months} months to repay this credit!")
elif calc_type == "a":
    print(f"Your annuity payment = {math.ceil(annuity_payment())}!")
elif calc_type == "p":
    print(f"Your credit principal = {round(credit_principal())}!")