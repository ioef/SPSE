#!/usr/bin/env python

from bs4 import BeautifulSoup 
import urllib


html = urllib.urlopen('http://www.securitytube.net/video/3000')

if html.code == 200:
	#Parse the html page using the lxml parser
	bt = BeautifulSoup(html.read(), 'lxml')

	#create a list with all the links in page searching for the a html tag
	links = bt.find_all('a')

	#fetch all the anchored text
	print
	print "Anchored Text found in the Website"
	print "=================================="
	
	for link in links:
		if link['href'] == '#':
			print link.string
