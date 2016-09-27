#!/usr/bin/env python

#Created by Dr_Ciphers
#Script that sends an ARP Request using the rawSockets
#
#Using the following Data:
#Destination MAC: ff:ff:ff:ff:ff:ff
#Source MAC: 00:0c:29:20:99:07
#Type: ARP 0x806
#Hardware Type: 0x0001
#Protocol Type: 0x0800
#Hardware Size: 0x06
#Protocol Size: 0x04
#Opcode Request: 0x0001
#Sender MAC: 00:0c:29:20:99:07
#Sender IP: c0a80202 (192.168.2.2)
#Target MAC:00:00:00:00:00:00
#Target IP: c0a80201 (192.168.2.1) 
#Padding: 18 Bytes of 00s


import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

rawSocket.bind(("eth1", socket.htons(0x0800)))

arpRequest = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s16s2s", '\xff\xff\xff\xff\xff\xff', '\x00\x0c\x29\x20\x99\x07', '\x08\x06','\x00\x01','\x08\x00','\x06','\x04','\x00\x01','\x00\x0c\x29\x20\x99\x07','\xc0\xa8\x02\02','\x00\x00\x00\x00\x00\x00','\xc0\xa8\x02\x01','\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00','\x00\x00')

rawSocket.send(arpRequest)

