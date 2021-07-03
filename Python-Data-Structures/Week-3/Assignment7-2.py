# Use the file name mbox-short.txt as the file name
fname = input("Enter File Name: ")
fh=open(fname)

cnt = 0
floatSum = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        cnt += 1
        findNum = line.find('0')
        x = line[findNum:]
        floatSum = floatSum + float(x)

average = float(floatSum/cnt)
print("Average spam confidence:",average)