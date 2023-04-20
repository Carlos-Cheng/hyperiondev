#This is a program is ask user for number of student and ID of each student, then print out a register form with dotted line for signature
#Create a blank register form
register_form = ""

#While loop to ask for number of student and prompt user reenter for invalid input
is_number = False
while is_number == False:
    try:
        student_number = float(input("how many students are registering?"))
    except:
        print("You are not entering a number!")
    else:
        if student_number < 0:
            print("Invalid input! You can't have negative number of student!")
        elif student_number == 0:
            print("Invalid input! if no student is registering, you do not need the form!")
        elif student_number != int(student_number):
            print("Invalid input! Please enter a whole number!")
        else:
            student_number = int(student_number)
            is_number = True
            break

#For loop to ask for student ID and add dotted line after
for i in range(student_number):
    student_id = input("What is the student ID?")
    register_form += student_id + "..............................\n"

#Try to write the form onto required text file, troubleshoot if fails
try:
    with open('reg_form.txt','w+') as f:
        f.write(register_form)
except:
    print("sorry something wrong with opening or writing file")

#End of program