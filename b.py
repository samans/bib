import string
import io
import re
import urllib.request

file = open('rfc.list', 'r')
for i in file.readlines():
    btname = "https://datatracker.ietf.org/doc/%s/bibtex/" % (i.strip())
    with urllib.request.urlopen(btname) as response:
        text = response.read().decode('utf-8')
        print (text.count('\n'))
        print( btname)
        print( text)

print( 'done\n')
