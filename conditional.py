#the conditional statements are : 
#1. if
#2. if else
#3. if elif else
#syntax of if statement
'''if condition:
    statement
    '''
#syntax of if else statement
'''if condition:
    statement
else:
    statement
    '''
#syntax of if elif else statement
'''if condition:
    statement
elif condition:
    statement
else:
    statement
    '''
    
#example of if statement
temp = int(input("Enter the temperature: "))
if temp > 25:
    print("its is a hot day")
elif temp > 15:
    print("it's a warm day")
else:
    print("it's a cold day")
    
#quiz
'''Write an if/elif/else statement for a college with a grading system as shown below:

If grade is 90 or higher, print "A"
Else if grade is 80 or higher, print "B"
Else if grade is 70 or higher, print "C"
Else if grade is 60 or higher, print "D"
Else, print "F" '''
grade = int(input("Enter your marks: "))
if grade > 100 or grade < 0:
    print("Invalid input")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")