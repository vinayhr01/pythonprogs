stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
app=org.split()
app.pop(0)
app.pop(1)
app.pop(3)
#print(app)
for wrd in app:
    asd=wrd.capitalize()
    #print(asd)
    for char in asd:
        zx=char.strip()
        aq=zx.find('O')
        if  aq==0:
            print(char)
        sd=zx.find('H')
        if sd==0:
            print(char)
        ds=zx.find('S')
        if ds==0:
            print(char)
        dv=zx.find('E')
        if dv==0:
            print(char)
acro=char
print(acro)
