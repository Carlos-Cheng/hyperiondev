#This is a program that validate user input two names when asked to enter full name
#define variables
first_name = input("please enter your first name")
last_name = input("please enter your last name")
full_name = first_name + last_name
length = len(full_name)

if first_name == "" or last_name == "": #check for input
    print("You haven't entered anything. Please enter your full name.")

elif length < 4: #check if less than 4 character
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

elif length > 25: #chek if more than 25 character
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

else: #print string for the desire input
    print("Thank you for entering your name.")

#end of program