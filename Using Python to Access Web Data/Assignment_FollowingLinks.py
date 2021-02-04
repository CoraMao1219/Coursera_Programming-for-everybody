import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Get count and position numbers
count = int(input('Enter count:'))
position = int(input('Enter position:'))

#Repeat the loop for the required counts
start = 0
while start < count:

    tags = soup('a')
    for tag in tags:
        tag = tags[position - 1].get('href', None) # Retrieve all of the anchor tags
    print("Retrieving:", tag)

    url = tag
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') #Update url through BeautifulSoup
    
    start = start + 1 #Update startcount by 1
