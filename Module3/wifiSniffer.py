#!/usr/bin/env python

#created by Dr Ciphers
#Before running this program the wlan0 card
#shall be set to monitor mode with a command like 
#sudo airmong-ng start wlan0
#Here we assume that the mon0 i/f is used

from scapy.all import *


def wificatcher(packets):
	for packet in packets:
		#check if Packet is a Beacon 
		if packet.haslayer(Dot11Beacon):
			if (packet[Dot11].addr3) and packet[Dot11].addr3 not in wifiList:
				wifiList.append(packet[Dot11].addr3)
				print "[+] Found SSID: %s with MAC:%s" %(packet[Dot11].info,packet[Dot11].addr3)
wifiList = []

sniff(iface = "mon0", prn=wificatcher)



