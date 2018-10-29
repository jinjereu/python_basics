# This is a comment in Python

# Printing
print("Hello, World!")

# Basic conditions showing indentation
if 5 > 2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")

# Assigning variables is inferential
x = "5"
y = "John"

print(x)
print(y)

# Strings can be concatenated with strings only
print(y + " has " + x + " apples. ")

# Operations can be done on numbers
a = 5
b = 6
print(a+b)

# Different Python numeric types
w = -87.7e100
x = 1
y = 2.8
z = 1j

print(type(w))
print(type(x))
print(type(y))
print(type(z))

# Casting can be done using the constructor functions int(), float(), str()

a = " Hello, world!"
# Retrieve character at index
print(a[1])
# Retrieve substring with start and end
print(a[2:5])
# strip whitespace
a = a.strip()
print(a)
# Length
print(len(a))
# lower() and upper() = lowercase/uppercase
print(a.lower())
# replace string
print(a.replace("Hello", "Whattsup"))
# split string
print(a.split(","))

# Command line input -> inpu()
#print("Enter your name:")
#name = input()
#print("Hello, " + name)

# Python arithmetics
# + - * / % ** //
# Python assignment operators
# = += -= *= /= %= //= **= &= |= ^= >>= <<=
# Python comparisons
# == != > >= <=
# Python logical
# and, or, not
# Python identity (Check if the same object)
# is, is not
# Python membership
# in, not in (Check if sequence is present in the object)

#Python collections
thislist = ["apple", "banana", "cherry"]
# or list(("one", "two", "three"))
for x in thislist:
    print(x)

#check if item is in list
if "apple" in thislist:
    print("Yes it is in the list")

#length of the list
print(len(thislist))

#append item
thislist.append("jackfruit")
print(thislist)

#insert item at position
thislist.insert(1, "orange")
print(thislist)

#remove specific tem
thislist.remove("banana")
print(thislist)

#remove last item. provide index removing specified index
thislist.pop()
print(thislist)

#delete the list
#del thislist

#empty the list
thislist.clear()
print(thislist)
