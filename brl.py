import string
import io
import re
import urllib.request

rfcList = list()
urlList = list()
titleList = list()
abstractList = list()
file = open('rfc.list', 'r')
for i in file.readlines():
    btname = "https://datatracker.ietf.org/doc/%s/bibtex/" % (i.strip())
    rfcList.append(i.strip())
    with urllib.request.urlopen(btname) as response:
        text = response.read().decode('utf-8')
        url=re.findall("url = .*,\n",text,re.MULTILINE)
        urlStr=re.findall("https:[a-zA-Z0-9\-\.\/]*", url[0])
        urlList.append(urlStr[0])
        title=re.findall("title = .*,\n",text,re.MULTILINE)
        titleStr=re.findall("{{.*}}", title[0])
        titleS=titleStr[0].replace("{", "")
        titleS=titleS.replace("}", "")
        titleList.append(titleS)
        abstract=re.findall("abstract = .*,\n",text,re.MULTILINE)
        abstractStr=re.findall("{.*}", abstract[0])
        abstractS=abstractStr[0].replace("{", "")
        abstractS=abstractS.replace("}", "")
        abstractList.append(abstractS)

count = 0
for rl in rfcList:
    print ("5G|IETF|"+titleList[count]+" ("+rl+")|"+abstractList[count]+"|RFC|"+urlList[count])
    count = count + 1
