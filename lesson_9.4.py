fh = open('files/mbox-short.txt')
lst = list()
counts = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    lst.append(words[1])
for name in lst:
    counts[name] = counts.get(name,0) + 1
maxcount = None
maxname = None
for name,count in counts.items():
    if maxcount is None or count > maxcount:
        maxname = name
        maxcount = count
print(maxname, maxcount)