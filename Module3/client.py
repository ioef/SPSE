#!/usr/bin/env python

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.connect((sys.argv[1], 9999))

while 1:
	userInput = raw_input("Please enter a string (give \"quit\" to exit): ")

	if userInput == "quit": break

	tcpSocket.send(userInput)
	print tcpSocket.recv(2048)


tcpSocket.close()
