# Install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code4/bs4.zip
# and unzip it in the same directory at the file you are importing it into
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # if website have SSL we need to do the next 3 lines

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() # pretty much returns the entire document (probably UTF-8)
soup = HeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a') # grabs all the anchor tags
for tag in tags: # for each tag in the list of tags
    print(tag.get('href', None)) # it grabs the href value
