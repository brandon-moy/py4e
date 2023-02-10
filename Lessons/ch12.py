# CH 12 Networked Programs

# Transport Control Protocol (TCP)
# built on top of IP (internet protocol)
# assumes IP might lost some data - stores and retransmits data if it seems to be lost
# handles "flow control" using a transmit window
# provides a nice reliable pipe

# Python has built-in support for TCP Sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
# Make connection to ^ host on port^

# Application Protocol
# Since TCP(and Python) giuves us a reliable socket, what do we want to do with the socket?
# What problem do we want to solve?

# Application Protocols - Mail, World Wide Web

# HTTP - Hypertext Transfer Protocol

# the dominant Application Layer Protocol on the internet
# Invented for the Web - to retrieve HTML, Images, Documents etc
# Extended to be data in addition to documents

# HTTP - set of rules to allow browsers to retrieve web documents

# http://www.dr-chuck.com/page1.htm
# http:// - protocol
# www.dr-chuck.com - host
# /page1.htm - page

# HTTP Request in Python
import socket # improts the socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creates the socket - string based that suitable across internet
mysock.connect(('data.pr4e.org', 80))
# connect to data.pr4e.org on port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # encode prepares the data
mysock.send(cmd) # sends the string of code

while True:
    data = mysock.recv(512) # receiving 512 characters at a time -> data we get is bytes
    if (len(data) < 1) : # if we get 0 cahracters we get the end of the stream
        break # if we get 0 characters we break out of the loop
    print(data.decode()) # we decode and print the data
mysock.close() # we close the socket

# response is similar to using HTTPie in the terminal to make a request

# About Characters and Strings . . . (text processing)

# ASCII - American Standard Code for Information Interchange

# Representing Simple Strings
# Each character is represented by a number between 0 and 256 stored in 8 bits of memory
# We refer to 8 bits of memory as a byte of memory
# the ord() function tells us teh numberic value of a simple ASCII character

print(ord('H')) # 72
print(ord('e')) # 101
print(ord('\n')) # 10

# Unicode - billions of characters for every language
# so large there is almost every character

# Multi-Bye Character
# to represent the wide range of characters computers must handle we represent characters with more than one bye
# UTF-16 fixed length - 2 bytes
# UTF-32 fixed length - 4 bytes
# UTF-8 1-4 bytes
  # upwards compatible with ASCII
  # automatic deterction between ASCII and UTF-8
  # UTF-8 is recommended practice for encoding data to be exchanged between systems

# Two kinds of strings in Python
# in Python 2.7.10, there were separate strings and unicode strings
# In Python 3 all strings are Unicode

# Python Strings to Bytes
# when we talk to an external resourcel ike a socket, we need to decode Python 3 strings
# this is where we use the decode() method

# Making HTTP easier with URLLib
# since HTTP is so common, we have a library that does all the socket work for us
import urllib.request, urllib.parse, urllib.error

# urlopen - takes a url as a string that automatically gets encoded
# makes a connection, encodes the get request, retrieves all the headers
# returns an object that looks like a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand: # for every line in the file (received in bytes)
    words = line.decode().strip() # decode each line in the file and strip whitespace

# Take it a step further? Count words in file
    counts = dict()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)

# You can then use this to read web pages HTML and make a browser to parse the
# elements

# Parsing HTML

# Web Scraping
# when a program or script pretends to be a browser and retrieves web pages,
# looks at those pages, extracts information, and then looks are more pages

# Wy scrape?
# pull data - particularly social data - who links to who?
# get your own data back out of some system
# monitor a site for new information
# spider the web to make a data base for a search engine

# there is some controversy about web page scraping and some sites are snippy about it
# republishing copyrighted information is not allowed
# violated ToS is not allowed

# Easy Way - Beautiful Soup
# you could do string searches the hard way
# or use the free software library called BeautifulSoup from www.crummy.com

# BeautifulSoup Installation
# you can install BeautifulSoup https://pypi.python.org/pypi/beautifulsoup4

# or download http://www.py4e.com/code3/bs4.zip
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a') # you can call the object like a function and say give me all the a tags
    for tag in tags: # loop through the tags
        print(tag.get('href', None)) # pull out the href of the a tags
