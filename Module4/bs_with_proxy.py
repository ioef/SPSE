#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup

site = 'http://www.sectools.org'
proxy = urllib2.ProxyHandler({'http':'217.182.6.229:80'})

opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

response = urllib2.urlopen(site)

html = response.read()

bs = BeautifulSoup(html, 'lxml')


a_href = bs.find_all('a')

for link in a_href:
    if link['href']:
        print link.text + ': ' + link['href']

