#!/usr/bin/env python

#created by Dr_Ciphers

import socket
import sys
import struct
import binascii
from optparse import OptionParser



def parseEtherHeader(raw_packets):
   	'''
	Bytes 0                5 6              11 12     14
              +--------+--------+--------+--------+---------+
              |     Ethernet    |   Ethernet      | Ethernet|
              |     Dest Port   |   Source Host   | Type    |
              +--------+--------+--------+--------+---------+
              |              Ethernet Packet Data           |
              +--------+--------+--------+--------+---------+

	The code extracts and unpacks the ethernet header in Big Endian form
	First 6 bytes : Destination MAC
	Next  6 bytes : Source MAC
	Last  2 bytes : Ether type
	'''
	ethernet_header = raw_packets[0][0:14]
	eth_hdr = struct.unpack("!6s6s2s", ethernet_header)
	dst = binascii.hexlify(eth_hdr[0])      # destination MAC address
	src = binascii.hexlify(eth_hdr[1])      # source Mac address
	eth_type = binascii.hexlify(eth_hdr[2]) # Ether Type (0800 => IP)
	return (dst, src, eth_type)



def parseIPHeader(raw_packets):
	'''
    	Bytes 0             1               2               3               4
    	Bits  0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |Version|  IHL  |Type of Service|          Total Length       |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |         Identification        |Flags|      Fragment Offset  |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |  Time to Live |    Protocol   |         Header Checksum     |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                       Source Address                        |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                    Destination Address                      |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                    Options                    |    Padding  |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	The code extracts and unpacks the IP header in Big Endian form
    	First 12 bytes:IP Header data
    	Next   4 bytes: Source IP Address
	Next   4 bytes: Destination IP Address
    	'''

	ipHeader = raw_packets[0][14:34]
 	#!Big Endian Form of 12 bytes, followed by 4 bytes and 4 bytes
	ip_hdr = struct.unpack("!12s4s4s",ipHeader)

	sourceIP = socket.inet_ntoa(ip_hdr[1])
	destIP = socket.inet_ntoa(ip_hdr[2])
	return (sourceIP, destIP)



def parseTCPHeader(raw_packets):
	'''
    	Bytes 0             1               2               3               4
	Bits  0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7
    	      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |          Source Port          |       Destination Port      |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                        Sequence Number                      |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                    Acknowledgment Number                    |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |  Data |           |U|A|P|R|S|F|                             |
              | Offset| Reserved  |R|C|S|S|Y|I|            Window           |
              |       |           |G|K|H|T|N|N|                             |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |           Checksum            |         Urgent Pointer      |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                    Options                    |    Padding  |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
              |                             data                            |
              +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
	'''

	tcpHeader = raw_packets[0][34:54]
	#2 unsigned INTS + 16 Bytes
	tcp_hdr = struct.unpack("!HH16s",tcpHeader)
	
	sourcePort = tcp_hdr[0]
	destPort = tcp_hdr[1]
 
	return  sourcePort, destPort


def parseData(raw_packets,sport,dport):

	data = raw_packets[0][54:]
	if sport == 80 or dport == 80:
		print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
		print "DataStream:" 
		print "{0}".format(hexdump(data))
		print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"


def createSocket():
	'''
	this function creates a raw socket
	@return: new socket
	'''
	try:
		s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x800))
        	#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	except IOError:
		print "can not create socket (you have to be rootsys.exit(-1)"
	        sys.exit(-1)
	return s
       


def hexdump(src, length=16):
	result=[]
	digits = 4 if isinstance(src,unicode) else 2
	
	for i in xrange(0, len(src), length):
		s = src[i:i+length]
		hexa = b' '.join(["%0*X"%(digits, ord(x)) for x in s])
		text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
		result.append( b"%04X  %-*s  %s" %(i, length*(digits + 1), hexa, text))

	return (b'\n'.join(result))

def main():

	parser = OptionParser()
	parser.add_option("--verbose", action="store_true", dest="verbose",  default=False, help="enable verbose output")
	(options, args) = parser.parse_args()
	
	if options.verbose: verbose = True
	else: verbose = False	

	rawSocket = createSocket()

	pkt = "dummy"	
	while pkt:
		try:
			pkt = rawSocket.recvfrom(2048)
			destMAC, sourceMAC, ethType = parseEtherHeader(pkt)
			sourceIP, destIP = parseIPHeader(pkt)
			sourcePort, destPort = parseTCPHeader(pkt) 

			print "[+] Source MAC:%s | Destination MAC:%s | Eth Type:%s" %(sourceMAC, destMAC, ethType)
			print "[+] Source IP  %s:%s Destination IP:port %s:%s" %(sourceIP, sourcePort, destIP, destPort)
			if verbose == True:
				parseData(pkt,sourcePort,destPort)
		
			print

		except KeyboardInterrupt:
			print "Terminating sniffer"
			sys.exit(0)	


if __name__ == "__main__":
	main()
