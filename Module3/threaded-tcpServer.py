#!/usr/bin/env python

import threading
import Queue 
import socket

class WorkerThread(threading.Thread):
    
        def __init__(self, queue):
                threading.Thread.__init__(self)
                self.queue = queue

        def run(self):
                print "Creating WorkerThread for a new client"
   		data ="Hello Client"
		client = self.queue.get()

		data = client.recv(1024)
		print "Client sent: %s"%data
		client.send(data)
		
		print "Closing connection..."
		client.close()


   
def main():
	noOfThreads = 10

	queue = Queue.Queue()

	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	tcp_socket.bind(("0.0.0.0",9000))
	tcp_socket.listen(10)

	while True:
		print "waiting for a client..."
		(client, (ip, port)) = tcp_socket.accept()
		print "Received connection from ip and port: %s:%s ->" % (ip,port)
        	
		queue.put(client)
	        clientThread = WorkerThread(queue)
        	clientThread.start()

	print "Shutting down server..."
	tcpSocket.close()
	

if __name__=="__main__":
	main()		
