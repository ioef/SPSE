#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A2:Cross-Site Scripting 

Threat Agents: Consider anyone who can send untrusted data to the system, including external
users, internal users, and administrators. 

Exploitability: Attacker sends text-based attack scripts that exploit the interpreter in the 
browser. Almost any source of data can be an attack vector, including internal sources such 
as data from the database.

The attacks take place to a local Multillidae platform which is installed in the Metasploitable2

Example Usage: ./a1.py http://192.168.1.10/mutillidae/index.php?page=user-info.php

created by: Dr Ciphers
'''

import mechanize
import sys


xssString = '<div id="xssVictim">Hello Victim</div>'


def xssTester(url):
    #create a browser object from the mechanize
    browser = mechanize.Browser()

    #open the url provided
    browser.open(url)

    browser.select_form(nr=0)

    #acquire all the text fields of the form
    #and fill them with xssString
    for field in browser.form.controls:
        if field.type == 'text' or field.type == 'password':
            browser.form[field.name] = xssString
          

    #submit the form
    browser.submit()


    response = browser.response().read()


    return response




def main():
    if len(sys.argv) !=2:
        print "Exiting... Usage: a1.py http://www.vulnerablesite.com"
        sys.exit(-1)

    url = sys.argv[1]
    

    results = xssTester(url)

    #if the initial xssString is found inside the web server response then 
    #the page is vulnerable
    if xssString in results:
        print "[+] The tested page is vulnerable to the XSS Cross side scripting attack!"
        
if __name__ =="__main__":
    main()
