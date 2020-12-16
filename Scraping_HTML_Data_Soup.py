# In this assignment you will write a Python program to use 
# urllib to read the HTML from the data files below, and parse 
# the data, extracting numbers and compute the sum of the numbers 
# in the filefrom urllib.request import urlopen


from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    list = re.findall('[1-9][0-9]*', str(tag))
    for num in list:
        total = total + int(num)
        
print(total)
    
    
