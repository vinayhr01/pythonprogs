import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url=input('Enter url:- ')
uh = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(uh)
asd=info['comments']

for item in asd:
    qw=float(item['count'])
    #print(qw)
    sum=sum+qw
print(sum)
