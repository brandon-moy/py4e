# Ch 8 Lists

# Algorithms - a set of rules or steps to solve a problem
# Data Structures - a particular way of organizing data in a computer

# List Contants
# Surround by square brackets and the elements are separated by a comma - similar to JS Arrays

# Get items from the index in square brackets
friends = [ 'Joe', 'Sally', 'Tom']
friends[0] # Joe

# Lists are MUTABLE
fruit = 'Banana'
x = fruit.lower()
print(x) # banana
lotto = [2, 14, 26, 41, 63]
print(lotto) # [2, 14, 26, 41, 63]
lotto[2] = 28
print(lotto) # [2, 14, 28, 41, 63]

# len() function takes a list as a parameter and returns the number of elements

# range function returns a list of nubmers that range 0 to parameter -1
print(range(4)) # [0, 1, 2, 3]
print(len(friends)) # 3
print(range(len(friends))) # [0, 1, 2]

# Concatenating lists using +
# We can create a new list by adding two existing lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]
print(a) # [1, 2, 3]

# Lists can be sliced using :
t = [9, 41, 12, 3, 74, 15]
print(t[1:3]) # [41, 12]
print(t[:4]) # [9, 41, 12, 3]

# Building a List from Scratch

# We can create an empty list and ADD elements with the append method
# Elements are added to the end with append

stuff = list()
print(stuff) # []
stuff.append('book')
print(stuff) # ['book]
stuff.append(99)
print(stuff) # ['book', 99]
stuff.append('cookie')
print(stuff) # ['book', 99, 'cookie']

# Is something in a List?
# we can use in or not in to check if they are in a list

some = [1, 9, 21, 10, 16]
9 in some # true
15 in some # false
20 not in some # true

# Lists are in Order
# a list can hold many items and they can be sorted with sort()

friends = [ 'Sally', 'Joe', 'Tom']
friends.sort()
print(friends) # ['Joe', 'Sally', 'Tom]

# Built-in Functions and Lists
# len() - gives length
# max() - largest value
# min() - smallest value
# sum() sums item in list

# split() breaks a string into parts and prodcues a list of strings
abc = 'With three words'
stuff = abc.split()
print(stuff) # ['With', 'three', 'words]
print(len(stuff)) # 3
print(stuff[0]) # 'With'
for w in stuff :
    print(w)

# if you do not specify a delimiter, multiple spaces are treated as ONE space
line = 'A lot          of spaces'
etc = line.split()
print(etc) # ['A', 'lot', 'of', 'spaces']
line = 'first;second;third'
thing = line.split()
print(thing) # ['first;second;third']
print(len(thing)) # 1
thing = line.split(';')
print(thing) # ['first', 'second', 'third']
