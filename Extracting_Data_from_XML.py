# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in the file.from urllib.request import 
# urlopen


from bs4 import BeautifulSoup
import ssl
import xml.etree.cElementTree as ET
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_987974.xml'
html = urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
total = sum([int(count.text) for count in tree.findall('comments/comment/count')])
print(total)

