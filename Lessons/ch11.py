# Regular Expressions (regex)

# A regular expression, also regex or regexp, provides a concies and flexible
# means for matching string of text, such as particular characters, words,
# or patterns of chharacters.

# regular expressions are written in a formal language that can be interpreted
# by a regular expression processor

# Understanding RegEx
# very powerful and cryptic
# fun when you understand
# a language unto themselves
# language of marker characters
# kind of an old school compact language

# RegEx Quick Guide
# ^ matches the BEGINNING of a line
# $ matches the END of a line
# . matches ANY character
# /s matches WHITESPACE
# /S matches NON-WHITESPACE
# * REPEATS a character 0 or more times
# *? REPEATS a character 0 or more times (non-greedy)
# + REPEATS a character one or more times
# +? REPEATS a character on or more times (non-greedy)
# [aeiou] Matches a single character in the listed SET
# [^XYS] Matches a single character NOT IN the listed SET
# [a-z0-9] The set of characters can include a RANGE
# ( Indicates where string EXTRACTION is to start
# ) Indicates where string EXTRACTION is to end

# You need to import the library before using with "import re"
# You can sue re.search() to see if a string matches a regex
# You can use re.findall() to extract portions of a string that matches your regex

# Normal
hand = open('filename.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

# Regex
import re
hand = open('filename.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line)
        print(line)

# Using re.search() like startswiuth()

# Normal
hand = open('filename.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# Regex
hand = open('filename.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) # the ^ checks to match BEGINNING of a line
        print(line)

# Wild card character

# . matches ANY character
# if you add * character, the character is "any number of itmes"

# returns any line that begins with X, some nubmer of characters, then a :
^X.*:
# ^ beginning of line
# X is character
# . is any charcter
# * is any number of times
# and then a :

# Fine-Tuning your match
# depending on how "clean" your data is and the purpose of application, you
# may want to narrow your match down a bit

# returns line begins with X-, some nubmer of non-whitespace chars, then :
^X-\S+:
# ^ beginning of line
# Matches X-
# \S are non-white space characters
# + one or more times
# : followed by a :

# Matching and Extracting Data

#re.search() returns a True/False depending on whether the string matches the regex
# if we want the matching strings to be extracted we use re.findall()

x = 'My 2 favorite numbers are 19 and 43'
y  re.findall('[0-9]+',x)
# [] operation a list of allowed character but looks for 1 character
# the + looks at the list of allowed characters looking for one or more character
# that matches
print(y)
#['2', '19', '42']

y = re.findall('[AEIOU]+', x)
print(y)
# none match so it returns an empty list []

# WWarning: Greedy Matching
# the repeat characters (* and +) push outward in both directions (greedy)
# to match the largest possible string
x = 'From: Using the : character'
y = re.findall('^F.+:', x) # somethign that starts with F, characters, ends with :
print(y)
# ['From: Using the :']
# Why is it the whole thing?
# Greeding matching looks for the larger string and took the outer : instead of
# the : after From

# Non-greedy matching
# if you add a ?, the + and * will pull back
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
# ['From:] the ? is the non-greedy and returns at the first end character found

# Find tuning String Extraction
# you can refine the match for re.findall() and separately determine which portion
# of the match is to be extracted by using parentheses

x ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+\S+', x) # \S is at least one non-whitespace character
print(y)
# ['stephen.marquard@uct.ac.za']

# parentheses are not part of the match-but they tell us where to start and stop
# what string to extract
y = re.findall('^From (\S+@\S+', x)
print(y)
# ['stephen.marquard@uct.ac.za']

# String Parsing Examples

# String Extraction
data ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# 21
sppos = data.find(' ', atpos)
print(sppos)
# 31
host = data[atpos+1 : sppos]
print(host)
# uct.ac.za

# Double Split Pattern
words = data.split()
email = words[1]
# stephen.marquard@uct.ac.za
pieces = email.split('@')
# ['stephen.marquard', 'uct.ac.za']
print(pieces[1])
# uct.ac.za

# Regex Version
y = re.findall('@([^ ]*', lin)
# starting at @
# selecting in parenthesis
# [ ] set of characters
# ^  that are a non-blank character
# * matches many of them
print(y)
# [;uct.ac.za']


# Even Cooler Regex - more refined

y = re.findall('^From .*@([^ ]*', lin)
# ^ start at beginning of a line
# looking for string 'From '
# . -> any number of charactes
# until an @ sign
# () start extracting
# ^  non blank characters
print(y)
# ['uct.ac.za]

# Escape Characters
# if you want a special regex character to just behave normally (most of the time)
# prefix it with a '\'

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
# \$ looking for a $ sign
# [0-9.] range of characters 0-9 and a .
# + including one or more character
print(y)
# ['$10.00']
