#This program reads names and birthdays frm DOB.txt

with open("DOB.txt", "r") as file:
    lines= file.readlines()

print ("Name:")

for line in lines:
    parts= line.split()
    name= " ".join(parts[0:2])
    print(name)

print("\nBirthdate:")

for line in lines:
    parts= line.split()
    birthdate= " ".join(parts[2:])
    print(birthdate) 