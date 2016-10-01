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


	#code that finds the IP subnet automatically
	ip_sub = str(conf.route)
	ip_sub = ip_sub.split('\n')

	ip =""
	for line in ip_sub:
		if ("eth0" in line) or ("eth1" in line):
			ip = line.split()[0]
			ip = ip.split(".")
			ip_prefix = ip[0]+'.' + ip[1]+'.' + ip[2] + '.'

	if ip=="":
		sys.exit()
		
	#end of code that finds the subnet automatically 

	print "\nARP Scanner - Scanning for Devices"
	print "======================================"
	for ip_suffix in range(1,255):
		ip = ip_prefix + str(ip_suffix)
	
		arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
		#wait for 1 second before timeout and suppress the emission messages with verbose=0
		arpResponse = srp1(arpRequest, timeout=1, verbose=0)

		if arpResponse:
			print ("IP: %s MAC: %s" %(arpResponse.psrc,arpResponse.hwsrc))


if __name__=="__main__":
	main()
