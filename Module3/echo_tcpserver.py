#!/usr/bin/env python

import socket


#create a TCP socket
tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#The socket shall be reusable, in order to be immediately available for reuse
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) 

bind_ip   = "0.0.0.0" 
bind_port = 9999

tcpSocket.bind((bind_ip,bind_port))
tcpSocket.listen(2)

print "Waiting for Client..."


connection, (ip, sock) = tcpSocket.accept()

print "Received connection from Client with IP: %s:%d" %(ip,sock)

a = connection.recv(1024)
print ("Received from the Client the message: %s" %a)

clientEcho = "ECHO: "+ a

connection.send(clientEcho)

connection.close()
