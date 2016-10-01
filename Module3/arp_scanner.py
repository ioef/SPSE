#!/usr/bin/env python

from scapy.all import *
from signal import *
import sys

#ARP Subnet Scanner


def ctrlc_handler(signum,frame):
	sys.exit(0)


signal(SIGINT,ctrlc_handler)



def main():
	signal(SIGINT,ctrlc_handler)
	
	print "\nARP Scanner - Scanning for Devices"
	print "======================================"
	for ip_suffix in range(1,255):
		ip = '192.168.2.' + str(ip_suffix)
	
		arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
		#wait for 1 second before timeout and suppress the emission messages with verbose=0
		arpResponse = srp1(arpRequest, timeout=1, verbose=0)

		if arpResponse:
			print ("IP: %s MAC: %s" %(arpResponse.psrc,arpResponse.hwsrc))


if __name__=="__main__":
	main()
