handle = open('files/mbox-short.txt')
counts = dict()
lst = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    hour = words[5].split(":")
    lst.append(hour[0])
for hour in lst:
    counts[hour] = counts.get(hour, 0) + 1

newlst = list()
for key, val in counts.items():
    tup = (key, val)
    newlst.append(tup)
newlst = sorted(newlst)

for val, key in newlst:
    print(val,key)