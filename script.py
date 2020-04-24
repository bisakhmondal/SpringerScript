import os
import re
import requests as req

# Reading the pdf
# os.system('less Springer\ Ebooks.pdf >> pdfDecode.txt')
##Decoding of pdf may vary system to system. So I have provided it.

## catching Source url
file=open('pdfDecode.txt','r')
contents=file.read()
urls=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', contents.lower())

## Getting the pdf download link :-D
links=[]
cntr=1;
for i in urls:
    print(f'Processing Url: {cntr} / {len(urls)}')
    cntr+=1
    res=req.get(i)
    book=re.findall('/content/pdf/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',res.text)
    links.append('https://link.springer.com'+book[0])

## saving the links
with open('links.txt','w') as wio:
    wio.write('\n'.join(links))

## Downloading....
cntr=1
for l in links:
    print(f'Downloading {cntr} / {len(links)}')
    os.system(f'wget {l}')
    cntr+=1

print('Complete..')