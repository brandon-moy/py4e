# Web Services

# Most common ways to represent data going between applications across networds
# XML and JSON

# XML
# eXtensible Markup Language
# primary purpose is to help information systems share structured data
# it started as a simplified subset of the Standard Generalized Markup Language (SGML)
# and is designed to be relatively human-legible

# tags - indicate beginning and ending of elements
# attributes - keyword/value pairs on the opening tag of XML
# serialize/deserialize

# XML Basis

# can only have 1 main root element
<person> # opening tag
  <name> # opening tag
    Chuck # text content
  </name> # closing tag
  <phone type="intl"> # opening tag
    +1 734 303 4456 # text content
  </phone> # closing tag
  <email hide="yes" /> # self closing tag with na attribute
</person> # closing tag


# Whitespace in XML
# line ends do not matter, white space only matters in attributes and text content

# XML Schema
# description of the legal format of an XML document
# expressed in terms of contraints on the structure and content of documents
# often used to specify a contract between systems
# if the piece of XML meets the specifcation of the Schmema - it is said to "validate"

# Many XML Schema Languages
# Document Type Definition (DTD)
# Standard Generalized Markup Language (SGML)
## XML Schema from W3C (XSD)

# XSD XML Schema (W3C spec)
# World Wide Web Consortium (W3C) version
# commonly called XSD because the file names end in .xsd

# XSD Structure
# xs:element
# xs:sequence
# xs:complexType

# XSD Schema
<xs:complexType name="person"> # requires a complexType (outermost) name person
  <xs:sequence> # sequence in this order
    <xs:element name="lastname" type="xs:string" /> # element named lastname that has a string content
    <xs:element name="age" type="xs:integer" /> # element named age that has an integer content
    <Xs:elemetn name="dateborn" type="xs:date" /> # element named dateborn that has a date content
  </xs:sequence> # end of sequence
<xs:complexType> # end of complexType

# XML that matches this
<person>
  <lastname>Severance</lastname>
  <age>17</age>
  <dateborn>2001-04-17</dateborn>
  # common to represent time in UTC/GMT give that servers are often scattered around the work
</person>

import xml.etree.ElementTree as ET
data = '''<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
  </person>'''

tree = ET.fromstring(data) # this becomes an object we can query data out of
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# JSON JavaScript Object Notation
# JSON represents data as nested "lists" and "dictionaries"
# liked because it is easier to make and read
import JSON
data = ''' {
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}''' # this comes as a string of JSON

info = json.loads(data) # then it comes back as a dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

# Service Oriented Approach
# most non-trivial web apps use services
# they use services from other apps
  # credit card charge
  # hotel resv system
# services publish "rules" applications must follow to make use of the server (API)

# Multiple Systems
# Initiall - two systems cooperate and split the problem
# as the data/service becomes useful - multiple apps want to use the information

# Web Services
# API - Application Program Interface
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    # takes the key and the value and encodes it to the url

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    # open the url
    data = uh.read().decode()
    # decode the url
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data) # parsing the json
    except:
        js = None # if there's nothing then we just set to None

    if not js or 'status' not in js or js['status'] ~= 'OK':
        # catching if there was an error and sending message to user
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    # printing information from the result
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
