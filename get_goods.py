#!/usr/bin/env python
# A first Python script
import sys
from HTMLParser import HTMLParser

if(len(sys.argv) < 2):
	print("usage: ./get_goods.py <result html>")
	sys.exit(0)

searchFile=sys.argv[1]
i=0

print("Parsing {0}".format(searchFile))

# create a subclass and override the handler methods
# <div id="J_goodsList"
class MyHTMLParser(HTMLParser):
	def  __init__(self):
		self.goodcount=0
		self.goodlines=[]

    def handle_starttag(self, tag, attrs):
		if(tag == 'div'):
			is_goodlist=False
			for attr in attrs:
			    if(len(attr) > 1 && attr[0] == 'id' && arr[1] == 'J_goodsList'):
					print " J_goodsList pos:", self.getpos()
					self.goodcount=1
    def handle_endtag(self, tag):
		if(tag == 'li'):
			print 'an item processed'
    #def handle_data(self, data):
        #print "Encountered some data  :", data

parser = MyHTMLParser()

with open(searchFile) as f:
	for line in f:
		parser.feed(line)

