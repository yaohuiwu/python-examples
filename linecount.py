#!/usr/bin/env python
import os
import sys
from os.path import join 

def linecount(targetdir='.', ext='.java'):
    totalfiles=0
    totallines=0
    
    for(dirname, subs, files) in os.walk(targetdir):
        for f in files:
            if f.endswith(ext):
                print f
                totalfiles +=1
                fpath=join(dirname, f)
                with open(fpath) as myfile:
                    totallines += len(myfile.readlines())
    return (totallines,totalfiles)

if __name__ == '__main__':
    #print sys.argv
    targetdir='.'
    ext='.java'
    if len(sys.argv) >= 2:
        targetdir=sys.argv[1]
    if len(sys.argv) >= 3:
        ext=sys.argv[2]
    
    (lc, fc)=linecount(targetdir, ext)
    print "count dir:", targetdir, "\ntype:", ext, "\nlines:", lc, "\nfiles:", fc
