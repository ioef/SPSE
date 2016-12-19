#!/usr/bin/env python

"""  
	Module 4: Attacking Web Applications
	Excercise - SQL Injection in the DVWA
"""

import sys
import mechanize
from bs4 import BeautifulSoup



def dvwa_login(url, form_number, user, passwd):
	pass


def dvwa_enum():
	pass
def dvwa_sqli():
	pass

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
	dvwai_login = 'http://' + ip_address + '/dvwa/login.php'
	security_setting_url = 'http://' + ip_address +'/dvwa/security.php'
	sqli_url = 'http://' + ip_address + '/dvwa/vulnerabilities/sqli/'
	sqli_blind_url = 'http://' + ip_address +'/dvwa/vulnerabilities/sqli_blind/'

	print sqli_url



if __name__ =="__main__":
	main()	
