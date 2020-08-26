stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
app=sent.split()
app.pop(0)
app.pop(2)
#print(app)
acro=""
for i in app:
    acro=acro+i[0].upper()+i[1].upper()+'.'
print(acro)
