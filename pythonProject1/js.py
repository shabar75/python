# import json
# data = '''
# {
# "name":"shabar",
# "phone" : {
# "type" : "intl",
# "number": "7006877641"
# },
# "email": {
# "hide": "yes"
# }
# }'''
# info = json.loads(data)
# print('name is :' , info["name"])
# print('ph number is : ', info["phone"])
# import json
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''
# info = json.loads(data)
# print('user counr:', len(info))
# for iteam in info:
#     print('name:', iteam['name'])
#     print('id :', iteam['id'])
#     print('attribute: ', iteam['x'])
# import urllib.request, json
#
# address = input('Enter url: ')
# print('Retrieving', address)
# url= urllib.request.urlopen(address)
# info = json.loads(url.read().decode())
#
# print('Retrieved', len(str(info)), 'characters')
# data = info.get("comments")
# #print(data)
# num = total = 0
# for i in range(len(data)):
#     tmp = data[i]
#     value = tmp.get("count")
#     num = num + 1
#     total = total + int(value)
# print("Count:",num)
# print("Sum:",total)
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    p_id = js['results'][0]['place_id']
    print(p_id)
    print(location)
