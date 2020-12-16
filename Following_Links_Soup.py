# In this assignment you will write a Python program that expands on https://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= values from the 
# anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the 
# process a number of times, and report the last name you find.from urllib.request import urlopen


from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Kael.html'

#to repeat 7 times#
for i in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    print(url)
    for tag in tags:
        count = count +1
   
        #make it stop at position 3#
        if count>18:
            break
        url = tag.get('href', None)

print(url)
   
  
    

    

