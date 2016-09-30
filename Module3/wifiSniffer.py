#!/usr/bin/env python


from scapy.all import *


packets = sniff(iface = "wlan0")


