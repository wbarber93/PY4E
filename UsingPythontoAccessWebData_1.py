import re
name = ('regex_sum_987970.txt')
handle = open(name)

lst = list()

for line in handle:
    num = re.findall('([0-9]+)', line)
    if len(num) ==0: continue
    for each in num:
        flt = int(each)
        lst.append(flt)

print(len(lst))
total = sum(lst)
print(total)