#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A3:Broken Authentication and Session Management 

Threat Agents: Consider anyone who can trick your users into submitting a request to your
website. Any website or other HTML feed that your users access could do this.

Exploitability: Attacker creates forged HTTP requests and tricks a victim into submitting
them via image tags, XSS, or numerous other techniques. If the user is authenticated, the attack succeeds.

Example Usage: ./a5.py 

created by: Dr Ciphers
'''

import mechanize
import sys


url ='http://192.168.1.10/mutillidae/index.php?page=add-to-your-blog.php'


