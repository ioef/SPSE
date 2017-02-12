#!/usr/bin/env python
#
# The CookieJar can be used in mechanize is order to create a list of Cookies.
# Usefulness: The Cookie list can be inherited from a mechanize Session to another.Therefore the 
# credentials provided initally can be reused by a subsequent session

import mechanize
import sys
from optparse import OptionParser



def urlOpen():
	br.
	pass


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

	#Create a CookieJar	
	cookiejar = mech.CookieJar()

if __name__ == "__main__":
	main()

