#!/usr/bin/env python

import sys
import signal
import socket 


#set the timer to 60 seconds as default 
timer = 2 


def alarm_handler(signum, frame):
	exit(0)



def main():
	
	bind_ip="0.0.0.0"
	bind_port=9999

	#set the timer to 60 seconds as default 
	timer = 2

	#create the server socket
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((bind_ip, bind_port))
	server.listen(1)
	
	if len(sys.argv) == 2:
		timer = int(sys.argv[1])

	print "[*] Listening on %s:%d for %d seconds" %(bind_ip, bind_port, timer)
	
	if len(sys.argv) > 1  and sys.argv[1] == int:
		timer = sys.argv[1]		
	
	#start the SIGALRM timer in order to terminate the server automatically after N seconds 
	#as stored in the timer variable
	signal.signal(signal.SIGALRM, alarm_handler)
	signal.alarm(timer)


	#server forever or until the alarm goes off :)
	while True:
		#Accept connections
		client, addr = server.accept()

	



if __name__ == '__main__':
	main()

