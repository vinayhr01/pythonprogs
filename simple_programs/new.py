import re
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
regex=r'^[a-z]$|^([a-z]).*\1$'
count=0
qwe=sentence.split()
#print(qwe)
for wds in qwe:
    #print(wds)
    if (re.search(regex,wds)):
        count=count+1
        same_letter_count=count
print(same_letter_count)
