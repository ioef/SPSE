#!/usr/bin/env python

from scapy.all import *
import sys


def checkAndPrint(synPacket):
	ACK = 0x10
	SYN = 0x02
	RST = 0x04

	response = sr1(synPacket,verbose=0,timeout=0.1)
	if response:
		if response[TCP].flags & ACK:
			if response[TCP].flags & SYN:
				openPorts.append(response[TCP].sport)


if len(sys.argv[0:]) != 3:
	print ("usage: ./syn_scanner ip_address port_number")
	sys.exit(-1)

targetIP = sys.argv[1]

allscan = False
if sys.argv[2] == "all":
	allscan = True
else:
	targetPort = int(sys.argv[2])

openPorts=[]

if allscan:
	for targPort in xrange(1,1024):

		percCalc = targPort/float(1024)*100
		sys.stdout.write("\r" +"Scanning completed: " +str(percCalc)+"%")
		sys.stdout.flush()
		synPacket = IP(dst=targetIP)/TCP(dport=targPort,flags="S")
		checkAndPrint(synPacket)
else:
	synPacket = IP(dst=targetIP)/TCP(dport=targetPort,flags="S")
	checkAndPrint(synPacket)

	
print ("Results")
print ("============================================")

print ("Found Open Ports:")
print '\n'.join([str(x) for x in openPorts])

