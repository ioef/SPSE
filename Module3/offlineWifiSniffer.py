#!/usr/bin/env python

#supress the scapy warnings
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys


def pktParser(pcapfile): 
	#read the packets from the pcap file one by one
	with PcapReader(pcapfile) as pcap_reader:
		for pkt in pcap_reader:
			if pkt.haslayer(TCP):
				rawData  = pkt.sprintf('%Raw.load%')
				username = re.findall('(?i)user(.*)',rawData)
				if username:
					print pkt.summary()
					print '[+] User Account: ' + str(username[0])	

def main():

	if len(sys.argv) != 2:
		print "./offlineWifiSniffer.py pcapfile.pcap"
		sys.exit(1)

	
	pcapfile  = sys.argv[1]
	
	pktParser(pcapfile)



if __name__ == '__main__':
	main()
	
