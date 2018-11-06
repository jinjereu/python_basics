# PYTHON LAMBDA
# A small anonymous function,



# PYTHON CLASSES/OBJECTS

class MyClass:
    #properties are values assigned to objects
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    # The init function is a built-in function to assign values to object properties
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods are functions that belongs to the object
    def myfunc(self):
        #self parameter is a reference to the class instance which can be used to access the properties
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print(p1.name)
print(p1.age)

# Modify Object Properties
p1.age = 40
print(p1.age)

# Deleting Object properties
del p1.age
# Output:  Person instance has no attribute 'age'
# print(p1.age)

# Deleting Objects
del p1
# Output: NameError: name 'p1' is not defined
# print(p1)

# PYTHON ITERATORS

# An iterator is an object that can be iterated upon
# An iterator is an object implementing the iterator protocol

# Iterable
# Strings, Lists, tuples, dictionaries and sets are iterable containers which means you can use the iter() method

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
# Prints apple
print(next(myit))
# Prints banana
print(next(myit))
# Prints cherry

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator (an iterable object)

for x in mytuple:
    print(x)

for x in mystr:
    print(x)

# Creating an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    # StopIteration
    # The iteration would go on forever if implemented in a for loop so this must be implemented

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)

#JSON to Python Dictionary
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse JSON:

y = json.loads(x)

# converts it to Python dictionary

print(y["age"])

# Python dictionary to object

# a Python object (dict):
a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# cdonver to JSON

b = json.dumps(a)

# the result is a JSON string
print(b)

# TRY EXCEPT

try:
    print(something)
except NameError:
    print("An Exception occurred")
except:
    print("Something else")
else: #if not errors were raised
    print("whatever")

#Finally to execute something regardless of error or not
#Useful when closing objects and cleaning resources 
try:
    f = open("file.txt")
    f.write("Lorem ipsum")
except:
    print("Something went wrong when writing")
finally:
    f.close()
