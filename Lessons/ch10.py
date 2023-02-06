# CH 10 Tuples

# Tuples are another kind of sequence that functions much like a list
# -they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
# Joseph
y = (1, 9, 2)
print(y)
# (1, 9, 2)

# Similar to lists BUT tuple are "immutable"

# Things NOT to do with tuples
# cannot sort, add, or change order of a tuple

# A Tale of Two Sequences
l = list()
print(dir(l))

t = tuple()
print(dir(t))

# Why use tuple?
# Because they do not have to build a complex structure to be modified, they
# are more efficient

# Tuple and Assignment
# We can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parenthesis
(x, y) = (4, 'fred')
print(y)
# fred
(a, b) = (99, 98)
print(a)
# 99

# Tuple and Dictionaries
# The items() method in dictionaries returns a list of (key, value) tuples
d = {'csev': 2, 'cwen': 4}
tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])

# Tuples are Comparable
# comparison operators work with tuples and other sequences. if first is equal,
# python goes on to the next element, and so on until it finds elements that differ

# Scans until it finds a definitive answer
(0, 1, 2) < (5, 1, 2) # 0 < 5
# True
(0, 1, 200000) < (0, 3, 4) # 0 == 0 so go next, 1 < 3 true
# True
('Jones', 'Sally') < ('Jones', 'Sam') # Jones == Jones -> S == S -> a == a -> l < m -> True
# True

# Sorting Lists of Tuples
# we can take advantage of the ability to sort a list of tuples to get a sorted
# version of a dictionary
# first sort the dictionary using items() method and sorted() function
d = {'a':10, 'b':1. 'c':22}
d.items()
# dict_items([('a', 10, ('c', 22), 'b', 1)])
sorted(d.items())
# dict_items([('a', 10, ('b', 1), 'c', 22)])

# Using sorted()
d = {'a':10, 'b':1. 'c':22}
t = sorted(d.items())
for k, v in sorted(d.items()) :
    print(k, v)
# a 10
# b 1
# c 22

# Sort by values instead of key?
# sor tby value with a for loop that creates a list of tuples
c = {'a':10, 'b':1. 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) ) # by reversing here it appends the tuple in value, key pair
print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse=True) # always sorts by first value in a tuple
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]

# Even shorted version
c = {'a':10, 'b':1. 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )
# [(1, 'b'), (10, 'a'), (22, 'c')]
