#!/usr/bin/env python

from scapy.all import *
import sys

ACK = 0x10
SYN = 0x02
RST = 0x04


if len(sys.argv[0:]) != 3:
	print "usage: ./syn_scanner ip_address port_number"
	sys.exit(-1)

targetIP = sys.argv[1]
targetPort = int(sys.argv[2])

synPacket = IP(dst=targetIP)/TCP(dport=targetPort,flags="S")


response = sr1(synPacket,verbose=0)

if response[TCP].flags & ACK :
	if response[TCP].flags & SYN:
		print "Received SYN Response! Port probably open!"
	elif response[TCP].flags & RST:
		print "Received RST Response! The Port is closed"
	else:
		print "Port is either closed or filtered!"


