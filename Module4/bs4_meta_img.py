#!/usr/bin/env python
#This scripts prints all the page metadata and the images links

import urllib
from bs4 import BeautifulSoup


htmlpage = urllib.urlopen('http://www.securitytube.net/video/3000')

#1st check if the page has been succesfully retrieved
if htmlpage.code == 200:
	
	bs = BeautifulSoup(htmlpage.read(), 'lxml')
	allmeta = bs.find_all('meta')
	allimg  = bs.find_all('img')
	
	metalen = len(allmeta)
	metaCounter = 1

	imglen = len(allimg)
	imgCounter = 1

	for meta in allmeta:
		metaName      = meta.get('name')
		metahttpEquiv = meta.get('http-equiv')
		metaContent   = meta.get('content')
		print	
		print "HTML meta Tag found:%s out of %s" %(metaCounter, metalen)
		print "====================================="
		if metaName:
			print "Name: %s"%metaName	
		if metahttpEquiv:
	 		print "http-Equiv: %s"%metahttpEquiv	
		if metaContent:
			print "Content: %s"%metaContent
		
		metaCounter += 1


	for img in allimg:
		src = img.get('src')
		print 	
		print "HTML img found:%s out of %s" %(imgCounter,imglen)
		print "============================="
		if src:
			print "Img Source: %s" %src
		imgCounter += 1	
