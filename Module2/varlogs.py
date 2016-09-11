#!/usr/bin/env python

with open("/var/log/syslog", "r") as f:	
	for line in f:
		if "usb" in line:
			print line

