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
