#In the project I will be prompt the user to enter a string and make each other letter into a uppercase. then every other word in lowercase.
from _pyrepl.commands import end

#===Example 1===
'''sentence= "Hello Shamea"
final_string = ""
for i in range (len(sentence)):

    if i % 2== 1:
        final_string += sentence[i].upper()
    else:
        final_string += sentence [i].lower()
print(final_string)'''

sentence= "I am learning to code"
words=sentence.split()

for i in range (len(words)):

    if i  % 2== 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
final_string =" ".join (words)
print (final_string)




