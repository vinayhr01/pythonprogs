fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count=0
dic=dict()

for line in fh:
    if line.startswith('From'):
        qwe=line.rstrip()
        asd=qwe.strip('From: ')
        zxc=asd.split()
        poi=zxc[0]
    for wds in zxc:
        dic[wds]=dic.get(wds,0)+1
print(wds,'5')
lar=-1
larwrd=None
for k,v in dic.items():
    #print(k,v)
    if v>lar:
        lar=v
        larwrd=k
#print(larwrd,lar)
