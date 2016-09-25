#!/usr/bin/env python

import socket
import struct
import binascii


'''
PF_PACKET: Packet Sockets are used to receive and send raw packats at the device driver (OSI L2) level.
SOCK_RAW: Packets including the Data Link Level header 
0x0800: Shows the code for the protocol of interest which is the IP Protocol
'''
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

#extract and print Ethernet Header
ethernetHeader = pkt[0][0:14]
#!Big Endian Form of 6 bytes, followed by 6 bytes and 2 bytes
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)
destMACAddr = binascii.hexlify(eth_hdr[0]).upper()
sourceMACAddr = binascii.hexlify(eth_hdr[1]).upper()
ethType = binascii.hexlify(eth_hdr[2])

print "Destination MAC:%s | Source MAC:%s | Eth Type:%s" %(destMACAddr, sourceMACAddr, ethType)


#Extract and print IP Header
ipHeader = pkt[0][14:34]
#!Big Endian Form of 12 bytes, followed by 4 bytes and 4 bytes
ip_hdr = struct.unpack("!12s4s4s",ipHeader)

sourceIP = socket.inet_ntoa(ip_hdr[1])
destIP = socket.inet_ntoa(ip_hdr[2])


tcpHeader = pkt[0][34:54]
#2 unsigned INTS + 16 Bytes
tcp_hdr = struct.unpack("!HH16s",tcpHeader)

sourcePort = tcp_hdr[0]
destPort = tcp_hdr[1]

print 'Source IP:Port %s:%s' %(sourceIP, sourcePort)
print 'Destination IP:Port %s:%s' %(destIP, destPort)

