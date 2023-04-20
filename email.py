### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email():
# Create the class, constructor and methods to create a new Email object.
    
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content) :
            self.email_address = email_address
            self.subject_line = subject_line
            self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox_list = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    global inbox_list
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email("welcome@hyperiondev.com",
                    "Welcome to HyperionDev!",
                    "Congratulations! we are excited to officially welcome you to hyperiondev" )
    email_2 = Email("no-reply@hyperiondev.com",
                    "Great work on the bootcamp!",
                    "Well done! we are excited to see your great work!")
    email_3 = Email("review-team@hyperiondev.com",
                    "Your excellent marks!",
                    "Great job! You scored 1/4 in part a")
    inbox_list = [email_1, email_2, email_3]
    return inbox_list

def list_emails():
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for (index, email) in enumerate(inbox_list):
        print(index, email.subject_line)

def read_email(index):
    
    # Create a function which displays a selected email.
    try:
        global inbox_list
        email = inbox_list[index]
        print(f"email address:\t{email.email_address}")
        print(f"subject line:\t{email.subject_line}")
        print(f"email content:\t{email.email_content}")
    except:
        print("The email you looking for does not exist")
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    else:
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
        return inbox_list

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        while True:
            try:
                index = float(input("Which email would you like to read? (Enter number)"))
                if index < 0:
                    print("index cannot be negative number")
                elif (int(index) != index):
                    print("Please enter an integer value")
                elif index > len(inbox_list):
                    print("Please enter a valid number")
                else:
                    index = int(index)
                    read_email(index)
                    break
            except:
                print("Please enter the number corresponding to the email")
        
    elif user_choice == 2:
        # add logic here to view unread emails
        display = ""
        for email in inbox_list:
            if email.has_been_read == False:
                display += f"{email.subject_line}\n"
        if display == "":
            print("You have read all your email")
        else:
            print(display)
            
    elif user_choice == 3:
        # add logic here to quit appplication
        menu = False
        print("Thank you, bye!")
        break

    else:
        print("Oops - incorrect input.")

exit()
#End of the program