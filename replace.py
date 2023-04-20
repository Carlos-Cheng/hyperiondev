#define sentence string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#update the string by replacing "!" with " ", and print the update
sentence_1 = sentence.replace("!"," ")
print(sentence_1)

#update the string by changing into upper case and print update
sentence_2 = sentence_1.upper()
print(sentence_2)

"""Sorry I'm not sure if the task mean printing the original sentence
(the one with !) or the capitalised one (sentence_2)
this will print capitalised one in reverse.
Comment below to print original in reverse"""
print(sentence_2[::-1])
#print(sentence[::-1])

#end of code