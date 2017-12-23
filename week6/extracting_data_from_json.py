import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving {}'.format(url))

data = urllib.request.urlopen(url).read().decode()
print('Retrieved {} characters'.format(len(data)))

js = json.loads(data)
counts = [int(comment['count']) for comment in js['comments']]

print('Count: {}'.format(len(counts)))
print('Sum: {}'.format(sum(counts)))
