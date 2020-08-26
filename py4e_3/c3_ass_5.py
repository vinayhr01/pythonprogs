import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url=input('Enter url:- ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst=tree.findall('comments/comment')
count=len(lst)
print('count:',count)

for el in lst:
    l=el.find('count').text
    n=float(l)
    sum=sum+n
print('Sum:',sum)
