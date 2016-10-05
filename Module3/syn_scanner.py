#!/usr/bin/env python

from scapy.all import *
import sys

ACK = 0x10
SYN = 0x02
RST = 0x04


targetIP = "192.168.2.3"
targetPort = int(sys.argv[1])

synPacket = IP(dst=targetIP)/TCP(dport=targetPort,flags="S")


response = sr1(synPacket,verbose=0)

if response[TCP].flags & ACK :
	if response[TCP].flags & SYN:
		print "Received SYN Response! Port probably open!"
	elif response[TCP].flags & RST:
		print "Received RST Response! The Port is closed"
	else:
		print "Port is either closed or filtered!"


