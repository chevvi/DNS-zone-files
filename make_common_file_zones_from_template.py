#!/usr/bin/python3

import sys
import subprocess
import fileinput

def isgoodipv4(s):
    pieces = s.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False 

def reverse(st): return st[::-1]
reverse = lambda st: st[::-1]

if isgoodipv4(sys.argv[1]) == True:
    print("OK")
    arpa=reverse(sys.argv[1])
    print("%s" %arpa)
    fileToSearch='templatecommon'
    textToSearch='templatecommon'
    textToReplace='123456789'
    with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(textToSearch, textToReplace), end='')
    subprocess.run(["mv", "templatecommon", "%s" %arpa])
    subprocess.run(["mv", "templatecommon.bak", "templatecommon"])
    subprocess.run(["svn", "add", "%s" %arpa])
    subprocess.run(["svn", "propset", "svn:keywords", "'Id'", "%s" %arpa])
    subprocess.run(["svn", "ci", "-m", "%s " %arpa])

