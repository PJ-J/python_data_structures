# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

output = fh.read()
output = output.rstrip()
upper = output.upper()
print(upper)


# 2nd part
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = line[19:]
    fl = float(num)
    total = total + fl    
    count = count + 1

print("Average spam confidence: " + str(total/count))

