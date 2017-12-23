import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')

content = urllib.request.urlopen(url).read()
tree = ET.fromstring(content)

counts = tree.findall('.//count')
counts_sum = sum([int(count.text) for count in counts])

print('Retrieving {}'.format(url))
print('Retrieved {} characters'.format(str(len(content))))
print('Count: {}'.format(str(len(counts))))
print('Sum: {}'.format(str(counts_sum)))
