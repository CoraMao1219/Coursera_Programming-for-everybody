import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Input
location = input("Enter location:")
print("Retrieving" + location)
data = urllib.request.urlopen(location, context = ctx).read()
info = json.loads(data)

#Extract count
count = 0
sum = 0
for item in info["comments"]:
    count = count + 1
    sum = sum + item["count"]
print("Count:", count)
print("Sum:", sum)
