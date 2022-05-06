fname = open('files/romeo.txt')
lst = list()

for line in fname:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in lst:
            lst.append(word)

lst.sort()   
print(lst)