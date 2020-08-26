import re
fname=input("Enter a filname: ")
if len(fname)<1:
    fname="regex_act.txt"
fh=open(fname)
tot=0
lst=list()
flst=list()
for l in fh:
    #print(l.rstrip())
    asd=re.findall('[0-9]+',l)
    #print(asd)
    lst.append(asd)
lst.sort(reverse=True)
#print(lst)
ass=lst.index(['104','3088'])
#print(ass)
qw=lst[:44]
#print(qw)
for el in qw:
    for ele in el:
        poi=float(ele)
        #print(poi)
        tot=tot+poi
print(tot)
