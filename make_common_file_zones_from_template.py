#!/usr/bin/python3

import sys
import subprocess
import fileinput

def isgoodipv4(s):
    pieces = s.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False 


fileToSearch='templatecommon'
textToSearch='templatecommon'
textToReplace='123456789'
with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')
subprocess.run(["mv", "templatecommon", "newarpa"])
subprocess.run(["mv", "templatecommon.bak", "templatecommon"])
subprocess.run(["svn", "add"," newarpa"])
