#This program ask for a string and change alternate chacter uppercase and other alternate character lower
#define variables
word = str(input("Please insert the word"))
word = word.split(" ")
new_word = []
length = len(word)
for i in range(length):
    if i%2 == 0:
        new_word.append(word[i].lower())
    elif i%2 == 1:
        new_word.append(word[i].upper())
    else:
        print("error")
new_word = " ".join(new_word)
print(new_word)