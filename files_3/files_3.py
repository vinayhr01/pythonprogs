fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count=0
for line in fh:
    if line.startswith("From ") :
        count=count+1
        asd=line.rstrip()
        qwe=asd[5:]
        zxc=qwe.split()
        cvb=zxc[0]
        print(cvb)
        continue

print("There were", count, "lines in the file with From as the first word")
