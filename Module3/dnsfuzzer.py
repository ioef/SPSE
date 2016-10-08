#!/usr/bin/env python

from scapy.all import *
import sys
import signal

def ctrl_handler(signum, frame):
	print "Terminating Fuzzing"
	sys.exit(0)


if len(sys.argv) != 3:
	print "usage: ./dnsfuzzer.py dns_server_IP eth0"
	sys.exit(-1)

destIP = sys.argv[1]
adapter = sys.argv[2]


signal.signal(signal.SIGINT, ctrl_handler)
print "Starting DNS Fuzzing"
print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"

while True:
    packet=IP(dst=destIP)/UDP()/fuzz(DNS())
    sr(packet, iface=sys.argv[2], verbose = 1, inter=1, timeout=1)
