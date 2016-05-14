import os
from os.path import *

totallines=0

for (dirname, subs, files) in os.walk('.'):
    print '[', dirname, ']'
    for f in files:
        #print f
        if f.endswith('.py'):
            fpath=join(dirname, f)
            print fpath
            with open(fpath) as myfile:
                totallines += len(myfile.readlines())

print "total lines of python code:", totallines

