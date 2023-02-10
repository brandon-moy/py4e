# JSON = JavaScript Object Notation

import json

# JSON turns an object into a string / uses string since they are universal
data = '''
{
  "name" : "Chuck",
  "phone" : {
      "type" : "intl",
      "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

# loads the JSON data and turns it into a dictionary to use in Python
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
