# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request,urllib.parse,urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

lst=[]
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter:- ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)
# Retrieve all of the anchor tags
tags = soup('a')
#print(tags)
for tag in tags:
    #print(tag.get('href'))
    asd=tag.contents
    #print(asd)
    for qw in asd:
        lst.append(qw)
        for i,wd in enumerate(lst):
            if wd=='Yash':
                lst[i]='Vinay.H.R'
for el in lst:
    print(el)
