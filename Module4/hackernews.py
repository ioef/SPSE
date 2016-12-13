#!/usr/bin/env python

#terminal based hackernews 

import urllib
from bs4 import BeautifulSoup

#http://stackoverflow.com/questions/2330245/python-change-text-color-in-shell

def hilite(string, color, bold):
	attr = []
	if color == "yellow":
		attr.append('33')
        else: 
		#color == "green":
        	attr.append('32')
    	if bold:
        	attr.append('1')
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
				print hilite("%s"% (record.string), "green", True)
				print hilite("%s"% (record['href']), "yellow", False)
				print

if __name__ == "__main__":
	main()

