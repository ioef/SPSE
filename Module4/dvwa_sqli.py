#!/usr/bin/env python

"""  
	Module 4: Attacking Web Applications
	Excercise - SQL Injection in the DVWA
"""

import sys
import mechanize
from bs4 import BeautifulSoup


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
	browser.select_form(nr=0)

	#set the credentials and submit the data to the authentication form	
	browser.form['username'] = user
	browser.form['password'] = passwd
	browser.submit()

	links_enum()	

def dvwa_sqli():
	pass

def forms_show():
	for form in browser.forms():
		print form

def links_enum():
	#page links enumeration function
	for link in browser.links():
		if "SQL Injection" in link.text or "DVWA Security" == link.text :
			print link.base_url.rstrip('index.php') + link.url.rstrip('.')
		
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
	dvwa_login_url = 'http://' + ip_address + '/dvwa/login.php'
	security_setting_url = 'http://' + ip_address +'/dvwa/security.php'
	sqli_url = 'http://' + ip_address + '/dvwa/vulnerabilities/sqli/'
	sqli_blind_url = 'http://' + ip_address +'/dvwa/vulnerabilities/sqli_blind/'

	#login to the DVWA page
	dvwa_login(dvwa_login_url, 0, "admin", "password")

	#lower the security settings

	#perform SQLI Attacks

	#Perform SQLI Blind Attacks


if __name__ =="__main__":
	main()
