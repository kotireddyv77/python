# The comments will start with hash symbol in python

''' Multiline comments
using single quotes '''

""" Multiline comments using double

quotes """

print("Welcome to python")
print("Lets enjoy the party with Python")

#Strings
first_name = "koti"
food = "Pizza"
email = "fakemail@fake.com"

print(f"Hello {first_name}")
print(f"I like {food}")
print(f"My mail id is : {email}")


#Integers
age = 40
weight = 82

print(f"I am {age} years old")
print(f"My current weight is {weight}")


#float
price = 10.99
distance = 4.5

print (f"The cost price is ${price}")
print(f"The distance is {distance}km")

#Boolean either True ot False
is_student = True
for_sale = True
is_online = True

if is_student:
    print("You are a student")
else:
    print("Your are not a student")

if for_sale:
    print("The item is availeable for sale")
else:
    print("The item not available for sale")

if is_online:
    print("Your are in online")
else:
    print("You are in offline")

#Type casting str() int() float() bool()
name = "Koti Reddy"
age = 40
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

#name = bool(name)
print(name)
print(type(name))

# = int(name) # String to integer type convertion error
print(type(name))
print(name)


#input() function reads the user data and return the string
name = input("What is your name ?: ")
#age = input("How old are you ?: ")
age = int(input("How old are you ?: "))


age = age + 1
print(type(age))

print(f"Your name is {name}")
print(f"You are{age} old")











