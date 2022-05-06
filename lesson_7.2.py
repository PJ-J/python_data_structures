# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

output = fh.read()
output = output.rstrip()
upper = output.upper()
print(upper)
