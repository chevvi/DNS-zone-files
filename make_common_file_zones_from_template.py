#!/usr/bin/python3

import sys
import subprocess
import fileinput
from config import infraDns
from config import slave

def isgoodipv4(s):
    pieces = s.split('.')
    if len(pieces) != 3: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False 

def reverse(st): return st[::-1]
reverse = lambda st: st[::-1]

if isgoodipv4(sys.argv[1]) == True:
    print("OK")
    arpa=".".join(reversed(sys.argv[1].split('.'))) +'.in-addr.arpa'
    print("%s" %arpa)
    fileToSearch='templatecommon'
    textToSearch='templatecommon'
    #textToReplace='123456789'
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, arpa), end='')
    subprocess.run(["mv", "templatecommon", "%s" %sys.argv[1]])
    subprocess.run(["mv", "templatecommon.bak", "templatecommon"])
    subprocess.run(["svn", "add", "%s" %sys.argv[1]])
    subprocess.run(["svn", "propset", "svn:keywords", "'Id'", "%s" %sys.argv[1]])
    subprocess.run(["svn", "ci", "-m", "%s " %sys.argv[1]])
    text='\nzone \"%s.S\" {\n\ttype slave;\n\tfile \"slave/%s.S\";\n\tmasters {' % (arpa, arpa)
    for ns in infraDns:
        text=text+str("\n\t\t%s; \t//%s" % (infraDns[ns], ns))
    f=open('text1.txt', 'a')
    f.write(text)
    f.write('\n\t};\n};\n')
    f.close()


