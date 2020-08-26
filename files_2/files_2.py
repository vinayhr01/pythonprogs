fname = input("Enter file name: ")
fh = open(fname)
poi = list()
for line in fh:
    wds=line.rstrip()
    asd=wds.split()
    poi.append(asd)
sdf=poi[0]+poi[1]+poi[2]+poi[3]
#print(sdf)
fsdf=list(set(sdf))
fsdf.sort()
print(fsdf)
