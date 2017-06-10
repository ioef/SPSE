#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup



def main():

	#open the page and store it to the xmlpage variable
	xmlpage = urllib.urlopen('https://www.defcon.org/defconrss.xml')
	
	#parse the xmlpage with the BeautifulSoup xml parser
	bs = BeautifulSoup(xmlpage,"xml")

	for item in bs.find_all('item'):
		#print the title of the item
		print item.title.string	
		#print only the link's text
		print item.link.text


if __name__ =="__main__":
	main()
