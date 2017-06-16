#!/usr/bin/env python
'''
This script is part of the scripts developed which test a Web Application against a number 
of vulnerabilities. It is a python implementation for the OWASP Top 10. 

This is focused on the A8: Failure to Restrict URL Access

Threat Agents: Anyone with network access can send your application a request. Could 
anonymous users access a private page or regular users a privileged page?

Exploitability:Attacker, who is an authorized system user, simply changes the URL to
a privileged page. Is access granted? Anonymous users could access private pages that are not protected

The attacks take place to a local Multillidae platform which is installed in the Metasploitable2
Example Usage: ./a8.py 

created by: Dr Ciphers
'''
import urllib
import re 

#the following function creates a wordlist
def wordlist(url):
    #fill the wordlist with common pages
    wordlist=['phpinfo.php']

    #first check the robots.txt to find if they 're trying to hide anything
    url = url + '/robots.txt'
    response = urllib.urlopen(url)

   
    lines = response.read()

    #create a regular expression that has 4 distinct groups 
    #It searches for the Disallow keyword followed by a whitespace or not,
    # it matches the ./ but doesn't capture it (therfore the group does not created)
    #and also matches the actual keyword which corresponds to a page in the site
    regx = re.compile('(Disallow:)([\s\S])(?:./)(\w+)')
 
    #find all the instances and create a match object
    mo = regx.findall(lines)

    #add the 3rd element of the match object to the wordlist
    for match in mo:
        wordlist.append(match[2])

    
    return wordlist


def bruteforcer(url, wordlist):
    
    for word in wordlist:
        brute_url = url + '/' + word 
        response = urllib.urlopen(brute_url)
         
        if response.code == 200:
            print '[+] Page %s is not protected!!!'%brute_url


#base url
url = 'http://192.168.1.10/mutillidae'

#create a wordlist for bruteforce
wlist = wordlist(url)
#call the bruteforcer
bruteforcer(url,wlist)
