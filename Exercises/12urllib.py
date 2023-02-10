import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# creating a handle
# do not need to encode, or make a get command
for line in fhand:
    print(line.decode().strip())
# reads line by line which comes in bytes
# we need to decode it
# then strip whitespace

# Counting words
counts = dict() # create a dictionary
for line in fhand: # looks at each line
    words = line.decode().split() # decodes the line and splits it at spaces to get each word
    for word in words: # for each word in the list of words
        counts[word] = counts.get(word, 0) + 1 # counts at the word, if it exists then + 1 to value, otherwise 0 + 1
print(counts) # returns the list of words and counts
