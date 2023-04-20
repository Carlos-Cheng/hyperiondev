# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#define function
def reg_user():
    '''Add a new user to the user.txt file'''

    # - Check if the new username already exist
    while True:

        # - Request input of a new username
        new_username = input("New Username: ")

        if new_username in username_password.keys():
            print("Username already exist! Try another one")
            continue
        
        else:
            break

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        else:
            break

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''
    task_number = 0 #user read task number, so this starts at 1 (0+1)
    list_number = -1 #python indice starts at 0 (-1 +1)
    number_dictionary = {} #to get a dictionary of task number correspond to its location in task_list
    for t in task_list:
        list_number += 1
        if t['username'] == curr_user:
            task_number += 1
            number_dictionary[task_number]=list_number
            disp_str = f"Task {task_number}\n" #added display task number
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            print("_"*30+"\n") #added line for clarity between tasks
    my_total_task = task_number #get total number of task the user has
    return my_total_task,number_dictionary

def choose_task():
    while True:
        try:
            task_number = int(input("select a task by entering the task number or return to the main nemu by entering '-1'"))
            if task_number == -1:
                break
            elif task_number == 0:
                print("Task number cannot be 0!")
            elif task_number <= my_total_task:
                list_number = number_dictionary[task_number]
                if task_list[list_number]['completed'] == True:
                    print("Task already marked as complete and cannot be edited")
                    continue
                else:
                    while True:
                        complete_or_edit = str(input('''Select one of the following options below:
                        c - mark the task as complete
                        e - edit the task
                        ''')).lower()
                        if (complete_or_edit == "c") or (complete_or_edit == "e"):
                            edit_task(list_number,complete_or_edit)
                            break
                        else:
                            print("Invalid input! Please enter 'c' or 'e'")
                            continue
            else:
                print("Task number not available")
        except:
            print("Invalid input! Please try again")

def edit_task(list_number,complete_or_edit):
    '''Allow user to complete or edit the task depend on input
    prompt the user to change username or due date
    and what to change into'''
    if complete_or_edit == "c":
        task_list[list_number]['completed'] = True

    elif complete_or_edit =="e":
        while True:
            username_or_due_date = str(input('''Please choose one of the following options:
            u - change the username of the person to whom the task is assigned
            d - change the due date of the task
            b - back to last menu
            '''))
            if username_or_due_date == "u":
                while True:
                    task_username = input("Name of person assigned to task: ")
                    if task_username not in username_password.keys():
                        print("User does not exist. Please enter a valid username")
                    else:
                        task_list[list_number]["username"] = task_username
                        break
                break

            elif username_or_due_date == "d":
                while True:
                    try:
                        task_due_date = input("Due date of task (YYYY-MM-DD): ")
                        due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                        task_list[list_number]["due_date"] = due_date_time
                        break

                    except ValueError:
                        print("Invalid datetime format. Please use the format specified")
                break
            
            elif username_or_due_date == "b":
                print("No change is made on task")
                break
            else:
                print("Invalid input! Please enter 'u' or ' d'")
                continue

    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully edited.")    

def generate_reports():
    #check if file exist and make sure user aware the file will be overwritten
    overwrite = "n"
    try:
        with open("task_overview.txt", "r") as task_overview_file:
            task_overview_file.read()
        with open("user_overview.txt", "r") as user_overview_file:
            user_overview_file.read()

    except:
        overwrite = "y"

    else:
        while True:
            print("Either or both 'task_overview.txt' or 'user_overview.txt' already exist")
            overwrite = str(input('''Please choose one of the following options:
            y - yes, overwrite the file
            n - no, go back to menu
            ''')).lower()
            if (overwrite == "y") or (overwrite == "n"):
                break
            else:
                print("Invalid input")
    finally: # generate the required file

        if overwrite == "y":

            total_task = 0
            completed_task = 0
            uncompleted_task = 0
            uncompleted_overdue_task = 0
            task_overview_str = ""
            total_user = 0
            user_str = ""

            for t in task_list:
                total_task += 1

                if t["completed"] == True:
                    completed_task += 1

                else:
                    uncompleted_task += 1

                    if t['due_date'] > datetime.today():
                        uncompleted_overdue_task += 1

            for user in username_password:
                total_user += 1
                user_total_task = 0
                user_completed_task = 0
                user_uncompleted_task = 0
                user_uncompleted_overdue_task = 0 
                for t in task_list:
                    try:
                        if t['username'] == user:
                            user_total_task += 1
                            if t["completed"] == True:
                                user_completed_task += 1
                            else:
                                user_uncompleted_task += 1
                                if t['due_date'] > date.today():
                                    user_uncompleted_overdue_task += 1
                    except:
                        pass
                if user_total_task == 0:
                    user_str += f'''
                    {user}
                    This user has no task\n'''

                else:
                    user_str += f'''
                    {user}\n
                    {user_total_task} tasks assigned to {user}\n
                    {user_total_task/total_task*100} % of the total number of tasks that have been assigned to {user}\n
                    {user_completed_task/user_total_task*100} % of the tasks assigned to {user} that have been completed\n
                    {user_uncompleted_task/user_total_task*100} % of the tasks assigned to {user} that must still be completed\n
                    {user_uncompleted_overdue_task/user_total_task*100} % of the tasks assigned to {user} that have not yet been completed and are overdue\n
                    \n'''
                user_str += ("\n"+("_"*30) + "\n")

            user_overview_str = f'''
            {total_user} users registered with task_manager.py
            {total_task} tasks that have been generated and tracked using task_manager.py
            \n'''
            user_overview_str += "_"*30
            user_overview_str += user_str

            
            with open("task_overview.txt", "w") as task_overview_file:
                if total_task == 0:
                    task_overview_str = "There is no task"
                else:
                    task_overview_str = f'''
                    {total_task} tasks have been generated and tracked using the task_manager.py
                    {completed_task} complete tasks
                    {uncompleted_task} uncomplete tasks
                    {uncompleted_overdue_task} tasks that haven't been completed and that are overdue
                    {uncompleted_task/total_task*100} % tasks that are incomplete
                    {uncompleted_overdue_task/total_task*100} % tasks that are overdue
                    '''
                task_overview_file.write(task_overview_str)

            with open("user_overview.txt", "w") as user_overview_file:
                user_overview_file.write(user_overview_str)
        else:
            pass

def display_stat(): 
    '''If the user is an admin they can display statistics about number of users
        and tasks.'''
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")    

    try:
        with open("task_overview.txt","r") as task_overview_file:
            print(task_overview_file.read())
        with open("user_overview.txt", "r") as user_overview_file:
            print(user_overview_file.read())

    except:
        try:
            generate_reports()
            with open("task_overview.txt","r") as task_overview_file:
                print(task_overview_file.read())
            with open("user_overview.txt", "r") as user_overview_file:
                print(user_overview_file.read())
        except:
            print("Something wrong with file handling")

while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        my_total_task,number_dictionary = view_mine()
        choose_task()
    
    elif menu == 'gr':
        generate_reports()
    
    elif menu == 'ds' and curr_user == 'admin': 
        display_stat()

    elif menu == 'e':
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please Try again")

exit()
#End of program