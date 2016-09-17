#!/usr/bin/env python

with open("/var/log/messages", "r") as f:	
	for line in f:
		if "usb" in line:
			print line.strip()

