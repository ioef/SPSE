#!/usr/bin/env python

from subprocess import call

#The main problem of the below python script is that it allows the skip any sanity checks in the input of data. 
#Therefore it would allow an attacker to input arbritary and potentially malicious data like SQL Injection.
#This is like handing a loaded submachine gun to a child. For a example on malicious user like Trudy could issue
#as a filename not_existent_filename; rm -rf *" 
#Or not_existent; cat /etc/passwd
#
#Use it at your own risk! 
filename = raw_input("Please provide a filename you want to view:")

call("cat" + filename, shell=True)




