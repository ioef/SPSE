#!/usr/bin/env python
#
# The CookieJar can be used in mechanize is order to create a list of Cookies.
# Usefulness: The Cookie list can be inherited from a mechanize Session to another.Therefore the 
# credentials provided initally can be reused by a subsequent session

import mechanize
import sys
from optparse import OptionParser


def urlOpen(url,username, password, submitted):
	global cookiejar
	#Check if the function is called for the 1st time
	#if it is not reuse the cookie previously created	
	if submitted == True:
		br = mechanize.Browser()
		br.set_cookiejar(cookiejar)	
		br.open(url)

		#select the 1st form
		br.select_form(nr=0)
		#fill in the credentials
		form['username'] = username
		form['password'] = password
		br.submit()
	else:
		br2 = mechanize.Browser()
		br2.set_cookiejar(cookiejar)
		br2.open(url)
		

def main():
	parser = OptionParser(usage="usage: %prog url [options]")
	
	parser.add_option('-u','--username',dest='username', help='Username for the login')
	parser.add_option('-p','--password',dest='password', help='Password for the login')
		
	(options, args) = parser.parse_args()

	if len(args) !=1:
		parser.error("Incorrect number of arguments provided!")
		#parser.print_help()
		sys.exit(1)

	hostname = args[0]

	username = options.username 
	password = options.password

	if not username:
		parser.error("No username provided")
		sys.exit(1)

	if not password:
		parser.error("No password provided")
		sys.exit(1)

	urlOpen(hostname, username, password, True)
	urlOpen(hostname, username, password, False)


if __name__ == "__main__":
        #Create a CookieJar    
	cookiejar = mechanize.CookieJar()
	main()

