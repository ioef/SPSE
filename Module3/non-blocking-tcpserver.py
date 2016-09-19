#!/usr/bin/env python

import socket
import select

bind_ip='0.0.0.0'
bind_port = 9999

tcpServer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcpServer_socket.bind((bind_ip, bind_port))
tcpServer_socket.listen(5)

print "Waiting for clients on ip %s:%d" %(bind_ip, bind_port)


insockets = [tcpServer_socket]

output = []

while True:
	readable, writeable, errors = select.select(insockets, output, insockets)
	
	for receivedSocket in readable:
		if receivedSocket == tcpServersock:
			client_socket, (address,port) = receivedSocket.accept()
			insockets.append(client_socket)
			print "Received connection from the %s:%d" %(address, port)
		else:
			data = receivedSocket.recv(1024)
			if data:
				receivedSocket.send(data)
			else:
				receivedSocket.close()
				insockets.remove(receivedSocket)
