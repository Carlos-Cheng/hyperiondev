#This program does simple calculation by asking user to enter two number and an operator or read previous equation in new file
#I read the page on w3schools on file handling
#infinitely loop the question cause unknown amount of equation or file
file = None
infinite_loop = True
save = ""
calculate = False
read = False
while infinite_loop == True:
    
    #user decision on to calcuate or to read
    choice = str(input("Would you like to calculate or read all equation from a new text file?(enter calculate or read)"))
    if choice.lower() == "calculate":
        calculate = True
    elif choice.lower() == "read":
        read = True
    elif choice.lower() == "end":
        infinite_loop == False
        break
    else: #error if unable to identify their input
        print("invalid input, please try again")
        continue

    #simple calcuation with 2 number and operator
    while calculate == True:
        calculate = False
        try :
            num_1 = float(input("Please input the first number"))
            num_2 = float(input("Please input the second number"))
            operator = str(input("Please insert operator (e.g.+,-,*,x,/)"))
        except : #error if user has non-numeric input
            print("invalid input, try again")
            break

        if operator == "+":
            ans = num_1 + num_2
        elif operator == "-":
            ans = num_1 - num_2
        elif operator == "*" or operator.lower() =="x":
            ans = num_1 * num_2
        elif operator == "/" and num_2 == 0: #error message for zero division error
            print("divsion by zero")
            break
        elif operator == "/" and num_2!= 0:
            ans = num_1 / num_2
        else: #error message if user has invalid operator
            print("invalid operator, please try again")
            continue
        
        save = str(num_1)+operator+str(num_2)+"="+str(ans)+"\n"
        print(ans)

        print("Where would you like to save this equation?")
        try:
            file_name = str(input("Please input a file name"))
            file = open(f"{file_name}.txt","a")
            file.write(save)
            file.close()
            save = ""
        except:
            print("Error with file")
        finally:
            break

    #read all of the equation in a new file
    while read == True:
        read = False
        file_name = str(input("Please input a file name"))
        try : #try opening the file
            file = open(f"{file_name}.txt","r")
            print(file.read())
            file.close()
            break
        except FileNotFoundError as error: #error message if not found
            print("file does not exist")
        except:
            print("something else went wrong")
        finally:
            break

#End of program