# Dictionaries

# What is a collection?
# A collection is nice because we can put more than one value in it

# What is not a "collection" ?
# most variables only have one value

# List
# linear collection ofv alues that stays in order

# Dictionary
# a "bag" of values, each with its own label
# most powerful data collection
# allow us to do fast database-like operations in Python
# Also known as-
# Associative Arrays - Perl / PHP
# Properties or Map or HashMap - Java
# Property Bag - C#/ .Net
# Objects - JavaScript

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
# {'money': 12, 'tissues': 75, 'candy': 3}
print(purse['candy'])
# 3
purse['candy'] = purse['candy'] + 2
print(purse)
# {'money': 12, 'tissues': 75, 'candy': 5}

# Many counters with a dictionary

# one common use of dictionaries is counting how often we see something
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
# { 'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
# {'csev' : 1, 'cwen': 2}

# Dictionary Tracebacks
# it is an error to reference a key which is not in the dictionary
# we canuse the in operator to see if a key is in the dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : # loops through each name
    if name not in counts: # sees if name exists in list orn ot
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# get() method for dictionaries

# the pattern of checking to see if a key is already in a dictionary and assuming
# a default value if key is not there

if name in counts:
    x = counts[name]
else :
    x = 0

x = counts.get(name, 0)

# Simplifying counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1 # if there is a value, take value OTHERWISE value is 0
    # then it adds one so then if no value the value is one, and if there is a value it increments
print(counts)

# Counting Words in Text
counts = dict()
print('Enter a line of text:')
line = input('') # takes an input of text

words = line.split() # separates text at each space

print('Words:', words) # prints the list
print('Counting. . .')
for word in words : # loops through words
    counts[word] = counts.get(word, 0) + 1 # checks if word is in counts and adds to the count
print('Counts', counts) # returns the dictionary with counts

# Retrieving a list of keys
jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
# ['jan', 'chuck', 'fred]
print(jjj.keys())
# ['jan', 'chuck', 'fred]
print(jjj.values())
# [100, 1, 42]
print(jjj.items())
# [('jan', 100), ('chuck', 1), ('fred', 42)]

# We loop through key-value pairs using "two" iteration variables
# each iteration, the first variable is the key and the second variable is the
# corresponding value for the key
for aaa,bbb in jjj.items() : # basically saying for key, value in items of the dictionary
    print(aaa, bbb)
