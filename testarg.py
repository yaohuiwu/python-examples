#!/usr/bin/env python
# A first Python script
import sys

print("printing sys.argv")
ct=0
for arg in sys.argv:
    # print "sys.argv[",ct, "]=",arg
    print("sys.argv[{0}]={1}".format(ct, arg))
    ct += 1

