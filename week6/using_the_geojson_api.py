import urllib.request, urllib.parse, urllib.error
import json

api_url = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
url = api_url + urllib.parse.urlencode({'address': address})
print('Retrieving {}'.format(url))

data = urllib.request.urlopen(url).read().decode()
print('Retrieved {} characters'.format(len(data)))

js = json.loads(data)
print('Place id {}'.format(js['results'][0]['place_id']))
