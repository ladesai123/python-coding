import random

"""import sys
print(sys.version)
"""



print("Hii Python")
print("Guido Van Rossum: creator of python")
#Python is an interpretted programming language

#Variables
a = 5 #variable of type int
name = "Peter" #str tyoe
b = 2.0 #Float
c = 3.45 #Double
x, y, z = "apple", "orange", "banana"
print(x)
x = y = z = "banana"
print(x)

#Unpacking a List easily
fruits = ["apple", "pear", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)

#What about string of strings
x = "Python is easy"
print(x)

x = "Python"
y = "is"
z = "easy"
print(x, y, z)#print(x + y + z)

#Local and Global Variables

x = "Awesome"

def new():
    global x #if mentioned global it is global
    x = "fantastic"
    print("Python is", x)
new()
print("Python is",x)

#Data Types in Python
x = "Hello chennai"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j #complex
print(type(x))
x = ["apple"]
print(type(x))
x = ("apple","banana")
print(type(x))
x = range(6)
print(type(x))
print(x)
x = {"name" : "Hari", "age" : 20}#Dict
x = {"apple", "charan", "singdha"}#Set
x = frozenset({"apple", "chinna"})#Frozen Set
x = True #Bool
x = b"Hello" #Bytes

#Float is decimal points 1 or more

#Random Integer
#import random
print(random.randrange(1,10))

#type casting
x = int(2.8)#2
x = float(2) #2.0
x = str(2)#'2'

#Python Strings
print("He is 'Jonny'")
print('He is "Jonny"')
a = """""mULTi line strings
hajhaaalj jfhf """

a = "Hello World"
print(a[1])#e

for x in "banana":
    print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)#True

#or

if "free" in txt:
    print("Yes,'free' is present")

#slicing of strings
b = "Hello World!"#index starting from 0
print(b[2:7]) #from index 2 to index 7
print(b[:7]) #from start
print(b[7:]) #from 7 upto end excluding index 7

#Modifying Strings

s = " sai teja "
print(s.upper())
print(s.lower())

print(s.strip()) #removes whitespaces if any

print(s.replace("e", "a"))

print(s.split(","))

#Strings cancatenation

s = "sai"
t = "teja"
u = s + t
print(u)

#f-strings in python

age = 21
print(f"My age is {age}")
print(f"The shirt price is {age:.2f}")#prints 21.00

print("Hey we are \"coding\"")  #add a backslash

#python all string methods saved for later..source w3shcools

#python operators

#Python Lists
my_List = {"akshay", "mohan", "karthik"}
print(my_List)
print(len(my_List))
this_list = list(("apple", "banana", "cherry"))
print(this_list[0])
print(this_list[-1])
print(this_list[2:5])#2 is included while 5 is excluded
if apple in this_list:
    print("Apple is there in the List")
#insert methods in list
this_list.insert(2, "water-melon")
#append adds at the last
this_list.append("graphes")
