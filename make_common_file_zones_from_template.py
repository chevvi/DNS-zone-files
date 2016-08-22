#!/usr/bin/python3

import subprocess
import fileinput


fileToSearch='templatecommon'
textToSearch='templatecommon'
textToReplace='123456789'
with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')
subprocess.run(["mv", "templatecommon", "newarpa"])
subprocess.run(["mv", "templatecommon.bak", "templatecommon"])
subprocess.run(["svn", "add"," newarpa"])
