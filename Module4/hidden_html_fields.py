#!/usr/bin/env python
"""  
	Module 4: Attacking Web Applications
	Excercise - Modify Hidden Fields to send arbritary data 
"""

import sys
import mechanize
from bs4 import BeautifulSoup




def main():
	# create a browser object
	browser = mechanize.Browser()

	# Set the Browse options in order to avoid 403 errors
	browser.set_handle_robots(False)

	#In case you would like to use cookies
	# Cookie Jar
	#cj = cookielib.LWPCookieJar()
	#browser.set_cookiejar(cj)

	#Follows refresh 0 but not hangs on refresh > 0
	#alternatively you may want to switch off the refreshing with browser.set_handle_refresh(False)
	browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	#set the browser headers
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 Firefox/3.6.0')]
	
	response = browser.open('http://www.google.com')

	if response.code == 200:


		print "\nBefore changing the hidden Language field"
		for form in browser.forms():
			print(form)


		# lets change the language field to hl=en field, readonly:
		browser.select_form(nr=0)

		#Ignore the readonly attribute of the fields	
		browser.form.set_all_readonly(False)


		browser.form['hl']='en'
		browser.submit()

		print "\nAfter changing the hidden Language field"
		for form in browser.forms():
			print(form)


if __name__ =="__main__":
	main()
