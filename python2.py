#Tuple ordering and length is unchangeable. Content can be updatable
thistuple = ("apple", "orange", "banana")
#OR alternatively through the constructor:
#thistuple = tuple(("1", "2", "3"))
print(thistuple)

#Access position through index
print(thistuple[1])

#Update value at index - not supported in older versions of python
#thistuple[1] = "blackcurrant"
#print(thistuple)

#Loop through the tuple items
for x in thistuple:
    print(x)

#Check if item exists
if "apple" in thistuple:
    print("Yes apple is in the tuple")

#Print the number of items
print(len(thistuple))

#You cannot add and remove items in the Tuple

#Some built in methods
#1. count() Returns the number of times a value occurs in a Tuple
#2. index() Searches and returns the index of where a value occurs in a tuple

#Sets - unordered and unindexed
thisset = {"apple", "banana", "cherry"}
#OR alternatively through the constructor:
#thisset = set(("1", "2", "3"))
print(thisset)

#Since sets are unindexed, items cannot be accessed by index
for x in thisset:
    print(x)

if "banana" in thisset:
    print("Banana is found")

#Items cannot be changed in a set but items can be added
thisset.add("orange")
print(thisset)

#Add multiple items
thisset.update(["mango", "grapes"])
print(thisset)

#Get length of the set
print(len(thisset))

#Remove item. Remove will throw an error if the item DNE but discard won't
thisset.remove("banana")
thisset.discard("grapes")
print(thisset)

#Empty the set
thisset.clear()
print(thisset)

#Remove the variable completely
del thisset
#print(thisset) this will cause an error

#There is a bunch of built-in methods that you can use on sets such as intersection, symmetric, union, etc

#Dictionaries - a collection which is unordered, changeable, indexed
thisdict = {
    "key": "value",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#OR alternatively through its constructor:
#thisdict = dict(brand="Ford", model="Mustang", year=1964)

print(thisdict)

#Accessing items
x = thisdict["model"]
print(x)
#Alternatively we can also use the get() method
x = thisdict.get("brand")
print(x)

#Change Values
thisdict["year"] = 2018

#Looping through dictionary
print("Print key names:")
for x in thisdict:
    print(x)

print("Printing the values:")
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

print("Loop through keys and values")
for x,y in thisdict.items():
    print(x, y)

#Check if key exists
if "model" in thisdict:
    print("'model' is one of the keys in thisdict")

#Length of dictionary
print(len(thisdict))

#Add items to the dictionary
thisdict["color"] = "red"
print(thisdict)

#Remove specific item
thisdict.pop("model")
#or del thisdict["model"]

#Remove last inserted item
#thisdict.popitem()

#Clear the contents of dictionary
thisdict.clear()
print(thisdict)

#There are a bunch of built-in methods available

# CONDITIONALS
a = 33
b = 200
if b > a:
    print("B is greater than a")
elif a == b:
    print("B is equal to a")
else:
    print("B is less than a")

#Short Hand

#If - in one line
if b > a: print("B is greater than A")

#else in one line
#print("A") if a > b else print("B")
#Above doesnt seem to be supported in python 2.7

#multiple else statements
#print("A") if a > b else print("=") if a == b else print("B")
#Above doesnt seem to be supported in python 2.7

if a < b and a == 33:
    print("Both conditions are true")

if a > b or b > a:
    print("At least one is true")

#WHILE LOOPS
#Execute statements as long as the condition is true
i = 1
while i < 6:
    print(i)
    if i == 5:
        break
    i += 1

#FOR LOOPS
#Iterate over a sequence
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)

#range() Returns a sequence of numbers starting from 0 by default and increments by 1 by default

#prints 0 to 5
for x in range(6):
    print(x)

#print 2 to 5
for x in range (2, 6):
    print(x)

#prints 2 to 29 incrementing by 3 and then print after the loop finishes
for x in range(2, 30, 3):
    print(x)
else:
    print("Completed")

#Nested loops and recursive functions are supported

#FUNCTIONS
def my_function():
    print("Hello from a function")

my_function()

#information can be passed to functions as parameters
def my_function(param):
    print(param + " Silapan")

my_function("Fernando")
my_function("Judith")
my_function("Lauro")

#providing default parameter values
def place_of_birth(country = "Norway"):
    print("I am from " + country)

place_of_birth("Germany")
place_of_birth()
place_of_birth("Estonia")
place_of_birth("Vanuatu")

#return values on functions
def my_function(x):
    return 5 * x

print(my_function(20))
print(my_function(5))
print(my_function(1))
