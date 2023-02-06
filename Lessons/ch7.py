# Reading Files

# File Processing
# A text file can be thought of as a sequence of lines

# Opening a File

# Before we can read the contents we must tell Python which file we are going to
# work with

# This is done iwth the open() function
# open() returns a "file handle" - a variable used to eprform operations on the file

# Using open()
# handle = open(filename, mode)

# returns a handle use to manipulate the file
# filename is a string
# mode is optional - 'r' is to read and 'w' is to write to the file

# What is a Handle?
# fhand = open('mbox.txt')
# print(fhand)
# This is like a wrapper that allows us to access the file  but is not the file itself

# Newline character
# we use a special character called "newline" to indicate when a line ends - \n

stuff = 'Hellow\nWorld!'
print(stuff)

# \n still counts as ONE character

# File Handle as a Sequence

# A file handle open for read can be treated as a sequence of strings where each
# line in the file is a string in the sequence

# We can sue for loop to iterate through a sequence - sequence is an ordered set

# Counting Lines in a file
# Open a file - read only
# Use a for loop for each line
# Count the lines and print the number of lines

fhand = open('filename.txt')
count = 0
for line in fhand :
    count = count + 1
print('Line Count:', count)

# We can read the whole file (newlines and all) into a single string
fhand = open('filename.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Searching Through a File
# We can put an if statementi n our for loop to only print lines that meet criteria
fhand = open('filename.txt')
for line in fhand:
    line = line.rstrip() # We can use rstrip() to remove the whitespace from right side
    if line.startswith('From:') :
        print(line)
