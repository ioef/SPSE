#!/usr/bin/env python

import socket
import multiprocessing


#create a function that handles the data received from the client
def clientHandler(client_socket,client_ip, client_port):
	data ="test"

	while data:
		data = client_socket.recv(1024)
		print "Received %s from Client %s:%d" %(data, client_ip, client_port)
		client_socket.send(data)
	
	client_socket.close()




def main():
	processing_list = []

	bind_ip="0.0.0.0"
	bind_port=9999

	tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	tcpServer.bind((bind_ip, bind_port))

	tcpServer.listen(5)
	
	#server forever
	while True:
		client_socket, (client_ip, client_port) = tcpServer.accept()
		
		process = multiprocessing.Process(target=clientHandler, args=(client_socket, client_ip, client_port))
		process.start()
		processing_list.append(process)

if __name__ == "__main__":
	main()
