#This is a program to ask user to enter a number until -1, then calculate average exclusing the -1
#Define variable number, total and tries
number = float(input("Please enter a number"))
total = 0
tries = 0

while number!= -1 : #Ask for input until -1
    total += number
    tries += 1
    number = float(input("Please enter a number"))

if tries == 0: #Avoid zero division error on first try
    print("You got -1 on first try!")

else: #Calculate average for non first try scenario
    average = total/tries
    print(f"The average of the numbers entered exclusing the -1 is{average}")

#End of program