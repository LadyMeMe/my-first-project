# This example program is meant to demonstrate errors.

#===example 1 ===

'''print "Welcome to the error program"
print "\n" '''

#SyntaxError: Missing parentheses in call to 'print'. Line 5
print("Welcome to the error program")
print ("\n")

# Example 2. with user's age, making the str to an int. Run error
'''age_str = "24 years old"
age = int (age_str)
print("I'm" + age + "years old.")'''

#Runtime Error: Line 13 age-Str == "24 years old. Cannot be converted into integer
'''age_str = "24"
age = int(age_str)
print(" I'm " + str (age) + " years old.")
#Runtime Error must be converted into a string.'''

#===example 3===
'''years_from_now = "3" #Runtime error "3" is a string but it needs to be a integer
total_years = age + years_from_now
print ("The total number of years:" + "answer_years") #Missing Parenthesis line 27, and cannot add and integer and a string together'''
age =24
years_from_now = 3
total_years = age + years_from_now
print ("The total number of years: " + str(total_years))
