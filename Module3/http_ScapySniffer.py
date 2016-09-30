#!/usr/bin/env python

#created by Dr_Ciphers

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

import signal


def prnpacket(packets):
	for packet in packets:
		#check if the packet has Payload
		if packet.haslayer(Raw):
		
			rawData= str(packet.getlayer(Raw))
	
			if rawData.startswith("GET"):
				print rawData								
			elif rawData.startswith("POST"):
				print rawData

def ctrlc_handler(signum,frame):
	print "Terminating Program..."
	sys.exit(0)


					
signal.signal(signal.SIGINT, ctrlc_handler)
packets = sniff(iface="eth1", filter="tcp port 80",prn=prnpacket)

