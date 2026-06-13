#This is a list of my 3 friends
friends_names= (["Shaneeka", "Tachelle", "Shala"])
print (friends_names[0]) #first friend
print (friends_names[-1]) #last friend

#The ages of the friends
friends_ages= [46, 45, 40.]
print (friends_names[0] + " is " + str(friends_ages[0]) + " years old")
print (friends_names[1] + " is " + str(friends_ages[1]) + " years old")
print (friends_names[2] + " is " + str(friends_ages[2]) + " years old")

#list of friends names
print (len (friends_names))

#Indexing
print (friends_names[0]) #prints at value 0 on the left
print (type(friends_names[1])) #print <class 'str>

#slicing the friends list
print (friends_names[1:4])
print (friends_names[ 1:2])

#changing elements to the list
friends_names= [" Shaneeka ", " Tachelle ", " Shala " ]
friends_names[1]= "LaJeana"
friends_names[0] = "Brittney"
print (friends_names)

#adding an element to the list
friends_names.append ("Nette")
print (friends_names)
friends_names.append ("Alia")
print (friends_names)

#deleting a element from the list
del friends_names[2]
print (friends_names)
del friends_names[1]
print (friends_names)

#checking if someone is on the list
print ("Shaneeka" in friends_names)
print ("Nette" in friends_names)

#Quickly populating list
age_list=[46] * 2
print (age_list)

#Casting  to a list
name="Shaneeka"
letters= list(name)
print (letters)