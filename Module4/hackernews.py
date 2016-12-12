#!/usr/bin/env python

#terminal based hackernews 

import urllib
from bs4 import BeautifulSoup



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
				print u"{0}".format(record.string)
				print record['href']
				print

if __name__ == "__main__":
	main()

