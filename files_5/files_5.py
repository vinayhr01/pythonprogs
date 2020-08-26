fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh=open(fname)
dict=dict()
for line in fh:
    line=line.rstrip()
    if line.startswith("From ") :
            wds=line.split()
            #print(wds)
            t=wds[5]
            #print(t)
            hrs=t[:2]
            #print(hrs)
            dict[hrs]=dict.get(hrs,0)+1
#for k,v in sorted (dict.items()) :
    #print(k,v)
