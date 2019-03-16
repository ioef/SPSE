#!/usr/bin/env python

import paramiko
import os
import sys
import getpass
import subprocess

user = getpass.getuser()


def transferFile(filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('localhost', username='demo')
    sftp = ssh.open_sftp()
    sftp.chdir('/pub/'+ user)
    sftp.listdir()
    sftp.put('/home/' + user + 'filename', 'destfile')
    ssh.close()


def main():
    filename =''
    os.chdir('/home/' + user)
    print os.getcwd()
    try:
        result = subprocess.call(["mvn", "clean"])    
        if result == 0:
            result = subprocess.call(["mvn", "install"])  
            if result !=0:
                print "[-] Error in compilation. Exiting"
                sys.exit(1)
    except:
        print "[-] Error in compilation! Exiting..."
        sys.exit(1)
   
    try:    
        transferFile(filename)
    except:
        print "[-] Error in transfer..."
        sys.exit(1)        


if __name__=="__main__":
    main()