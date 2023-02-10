# Open a socket, send a command, and retrieve the data
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# file handle that doesn't have any data yet
mysock.connect(('data.pr4e.org', 80))
# function call with a tuple
# connecting socket to a destination on internet with that domain
# second parameter is the port number - port 80
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# HTTP command
# need encode() due to string in python as unicode that needs to be convereted to UTF-8
mysock.send(cmd)
# after we make the connection, we send the response

while True:
    data = mysock.recv(512) # ask for up to 512 characters
    if (len(data) < 1): # end of file if we get no data back
        break
    print(data.decode()) # otherwise we decode the data from UTF-8 to unicode
mysock.close() # then we close the connection when we finish
