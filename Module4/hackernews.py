#!/usr/bin/env python

"""  
	Module 4: Attacking Web Applications
	Excercise - Beautiful Soup based HTML Parsing, Terminal based hackernews
"""

import urllib
from bs4 import BeautifulSoup

#http://stackoverflow.com/questions/2330245/python-change-text-color-in-shell

def hilite(string, color, bold):
	attr = []

	if color == "red":
		attr.append('31')
	elif color == "green":
		attr.append('32')
	elif color == "yellow":
		attr.append('33')
	elif color == "blue":
		attr.append('34')
	elif color == "purple":
		attr.append('35')
	elif color == "cyan":
		attr.append('36')
	elif color == "white":
		attr.append('37')
        else: 
		#color == "none":
        	attr.append('0')
    	if bold:
        	attr.append('1')	

	#return a form that is used in linux bash shell for the font and color settings
	#\xb1b[color;fontsizem;text\x1b[0m
	return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)


def main():
	#fetch the html page
	htmlpage = urllib.urlopen('http://news.ycombinator.com')

	if htmlpage.code == 200:
		#parse the page with bs
		bs = BeautifulSoup(htmlpage, 'lxml')

		#fetch all links that are story links
		links = bs.find_all('a', {'class': 'storylink'})

		print 
		for record in links:
			if record:
				print hilite("%s"% (record.string), "cyan", True)
				print hilite("%s"% (record['href']), "yellow", False)
				print

if __name__ == "__main__":
	main()

