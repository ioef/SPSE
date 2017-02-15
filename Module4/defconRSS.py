#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup



xmlpage = urllib.urlopen('https://www.defcon.org/defconrss.xml')

bs = BeautifulSoup(xmlpage,"xml")


for item in bs.find_all('item'):
	#print the title of the item
	print item.title.string
	#print only the link's text
	print item.link.text

