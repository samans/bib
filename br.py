import string
import io
import re
import urllib.request

rfcList = list()
urlList = list()
file = open('rfc.test', 'r')
for i in file.readlines():
    btname = "https://datatracker.ietf.org/doc/%s/bibtex/" % (i.strip())
    rfcList.append(i.strip())
    with urllib.request.urlopen(btname) as response:
        text = response.read().decode('utf-8')
        url=re.findall("url = .*,\n",text,re.MULTILINE)
        urlList.append(url[0])

count = 0
for rl in rfcList:
    print (rl + " " + urlList[count] + "\n")
    count = count + 1
    
print( 'done\n')
