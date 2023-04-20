#This is a program to read the DOB file in a list of names and a list of date of birth
#create the required lists
name_list = "Name\n"
DOB_list = "DOB\n"

#open and read file and add item to corresponding lists
with open('DOB.txt','r') as f:
    for line in f:
        line_item = line.split()
        name_list += line_item[0] + " " + line_item [1] + "\n"
        DOB_list += line_item[2] + " " + line_item[3] + " " + line_item[4] + "\n"

#display the resulting lists
print(name_list)
print(DOB_list)

#end of program