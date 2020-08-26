fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    y=line[20:]
    n=float(y)
    count=count+1
    tot=tot+n
avg=float(tot)/float(count)
print("Average spam confidence:",avg)
