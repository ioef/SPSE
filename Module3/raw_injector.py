#!/usr/bin/env python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))


#define the interface you want to perform the packet injection
#along with the protocol value instead of the port 
rawSocket.bind(("eth0", socket.htons(0x0800)))


#pack 6bytes with the destination MAC address, 6 bytes with the source MAC address
#and 2bytes with the ethernet Type which should be IP
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')


rawSocket.send(packet + "Hello There! This is the payload")

print "The Ethernet Header + the payload was sent!"

