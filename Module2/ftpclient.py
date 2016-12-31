#!/usr/bin/env python

import socket
import sys
from ftplib import FTP 

TIMEOUT = 1

def ftpIPs():
	ipList = []
	with open('ftpsites.txt','r') as ftpsites:
		for line in ftpsites:
			ipList.append(line.strip('\n'))

	return ipList

def main():

	
	serverIPList = ftpIPs()

	for serverIP in serverIPList:
		clientBanner = '\n[+] Attempting to connect to ftp server with IP: '  + serverIP + '\n'
		sys.stdout.write(clientBanner)
		ftp = FTP()

		if ftp == None:
			continue		

		try:
			ftp.connect(serverIP,21,TIMEOUT)	
			ftp.login()

			sys.stdout.write(ftp.getwelcome())
			sys.stdout.write(ftp.retrlines('LIST'))
			ftp.close()
			sys.stdout.write('\n')
 
		except: 
			continue 

if __name__ == "__main__":
	main()

