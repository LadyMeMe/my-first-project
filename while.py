#This assignment ask to write a program that ask theuser to enter a number.
#then calculates the average of the valid numbers entered.
#the program stops when the user enters -1
# the number 0 is ignored. 

total=0
count=0
while True: 
    num= int(input(" Enter a number "))
    if num == -1:
        break
    if num == 0:
        continue
    total += num
    count += 1
if count> 0:
    average =total/count
    print(" the average is:", average)
else:
    print(" No valid numbers entered.")