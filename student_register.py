#This program registers students for an exam venue. 

num_students = int(input("How many students do you want to register? "))

with open("reg_form.txt", "w") as file:
    for i in range(num_students):
        student_ID = input ("Enter student ID number: ")
        file.write(student_ID + "\n")
        file.write ("................\n")