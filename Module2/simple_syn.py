#!/usr/bin/env python

from scapy.all import *
import sys

if len(sys.argv) !=3:
    print "Invalid number of arguments"
    sys.exit(1)

ip=sys.argv[1]
port=int(sys.argv[2])


response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)

if response:
    if response[TCP].flags == 18:
            print "[+] PortNumber %s OPEN"%port
