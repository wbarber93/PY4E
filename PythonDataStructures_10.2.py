# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. You can 
# pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
lst = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From "): continue
    line = line.split()
    time = line[5]
    hour = time.split(":")[0]
    count[hour] = count.get(hour, 0) + 1  
  

for key,val in count.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for val, key in lst:
    print(val, key)
