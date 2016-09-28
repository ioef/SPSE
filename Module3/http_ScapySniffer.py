#!/usr/bin/env python

from scapy.all import *

def prnpacket(packet):
	for i in range(len(packet)):
		if packet[i].haslayer(Raw):
			s = packet[i].load.split('\r\n')
	
			for i in range(len(s)):
				print s[i]


packets = sniff(iface="eth1", filter="tcp port 80", count=30)

prnpacket(packets)


