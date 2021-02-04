import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Input
location = input('Enter location:')
print('Retrieving' + location)
data = urllib.request.urlopen(location, context = ctx).read()
tree = ET.fromstring(data)

#Extract count
lst = tree.findall('.//count')
sum = 0
for item in lst:
    sum = sum + int(item.text)

print('Sum:', sum)
