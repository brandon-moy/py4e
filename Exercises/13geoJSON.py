import urllib.request, urllib.parse, urllib.error
import json

# service url from documentation
service url = 'http://maps.googleapis.com/maps.api/geocode/json?'

while True:
    # user provides a location
    address = input('Enter location: ')
    if len(address) < 1: break

    # concatenate the service url with the urlencoded address for the api
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    # open to get a handle
    uh = urllib.request.urlopen(url)
    # read and decode the document
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # checking the status of the response
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    # opposite of loads and indents
    print(json.dumps(js, indent=4))

    # prints results to user
    # often need to check response of data to determine how to access what data
    # we want to return
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)
