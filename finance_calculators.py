import math

#ask and validate input
print('''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed
''')
user_input = str(input("Enter either 'investment' or 'bond' from the menu above to proceed")).lower()

#both branch define variable and apply formula

    #investment branch of function
if user_input == "investment":
    P = int(input("how much are you depositing?"))
    r = str(input("What is the interest rate (%)?"))
    r = r.strip("%")
    r = int(r)/100
    t = int(input("How many years are you investing in?"))
    interest = str(input("Do you want simple or compound interest?"))
    if interest == "simple":
        A = P*(1+r*t)
    elif interest == "compound":
            A = P * math.pow((1+r),t)
    else:
        print("invalid input")
    print(f"Total amount once interest applied = {A} ")

#bond branch of function
elif user_input == "bond":
    P = int(input("What is the present value of the house?"))
    i = str(input("What is the interest rate (%)?"))
    i = i.strip("%")
    i = int(i)/100
    i = i/12
    n = int(input("How many month do you plan to repay the bond"))
    repayment = (i*P)/(1-(1+i)**(-n))
    print(f"You have to repay {repayment} each month")

#invalid input
else:
    print("Please enter either 'investment' or 'bond'")

#end of program
