# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for data in fh.readlines():
    print(data.upper().rstrip())