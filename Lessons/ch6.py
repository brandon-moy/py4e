# Ch 6 Strings

# Looking Inside Strings
# We can get at any character using an index specified in square brackets

fruit = 'banana'
letter = fruit[1]
print(letter) # prints a

x = 3
w = fruit[x-1]
print(w) # prints n

# Python throws error if you try to go beyond the end of a string

# Looping through strings
# using a while statement and an iteration variable, and the len function,
# we can construct al oop to lok at each of the letters in a string individually

index = 0;
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# for loop - definite loop using a for statement

for letter in fruit :
    print(letter)

# Generally the for loop is beetter because it is more "elegant" and uses less
# code which makes it cleaner and less likely to run into an error

# Looping and counting

count = 0
for letter in fruit :
  if letter == 'a' :
      count = count + 1
print(count)

# Looking deeper into in
# The iteration variable "iterates" through the sequence
# the block (body) of code is executed once for each value *IN* the sequence
# the iteration variable moves through all of the values *IN* the sequence

# Slicing Strings

# We can look at continuous section of a string using a colon operator
# Second number is one beyond the end of the slice - up to but not including
# if the second number is beyond the end of the string, it stops at the end

s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python

# If you omit first, it assumes beginning
# If you omit last, it assumes end
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python

# Using IN as a logical operator
# in keyword can also be used to check to see if one string is "in" another string
# returns a boolean

'n' in fruit # True (fruit is banana)
'm' in fruit # False
'nan' in fruit # True
if 'a' in fruit :
    print('Found it!') # Found it!

# String Comparison
word = 'apple';
if word =='banana':
    print('All right, bananas.')

if word < 'banana' :
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana' :
    print('Your word, ' + word + ', comes after banana.')
else: print('All right, bananas.')

# String functions/methods

# .lower(), .upper(). . .
# strings are immutable, these methods return a new string that has been altered
greet = 'Hello Bob'
zap = greet.lower();
print(zap) # hello bob
print(greet) # Hello Bob

print('Hi There'.lower()) # hi there

# dir(variable_of_data_type)
# dir displays all of the build in methods for that type

# find() - searches for a substring within another string - finds the first occurance
# if nothign is found -1 is returned

pos = fruit.find('na')
print(pos) # returns 2

# Search and replace
# replace() is like search and replace - it replaces ALL OCCURRENCES of the
# search string with the replacement string

nstr = greet.replace('Bob', 'Jane')
print(nstr) # Hello Jane

nstr = greet.replace('o', 'X')
print(nstr) # HellX BXB

# Stripping Whitespace
# sometimes we want to take a string and remove whitespace at the beginning/end
# lstrip() and rstrip() remove at the left or right
# strip() removes both

greet = '    Hello Bob    '
greet.lstrip() # 'Hello Bob    '
greet.rstrip() # '    Hello Bob'
greet.strip() # 'Hello Bob'

# Prefixes
line = 'Please have a nice day'
line.startswith('Please') # True
line.startswith('p') # False

# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:1416 2008'
atpos = data.find('@')
print(atpos) # 21

sppos = data.find(' ', atpos) # Find a space starting at the atpos
print(sppos) # 31

host = data[atpos+1 : sppos]
print(host) # uct.ac.za
