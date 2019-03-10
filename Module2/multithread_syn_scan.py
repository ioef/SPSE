#!/usr/bin/env python

import threading
from scapy.all import * 
import Queue
import time 

ip="192.168.0.1"

class WorkerThread(threading.Thread):
	
	def __init__(self, queue, outqueue):
		threading.Thread.__init__(self)
		self.queue = queue
                self.outqueue = outqueue

        def scanner(self, ip, port):

            response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
            if response:
                if response[TCP].flags == 18:
                    return "[+] PortNumber %s OPEN"%port

	def run(self):
	      #print "In WorkerThread"
	
		step = 0
		while True:
			port = self.queue.get()
                        result = self.scanner(ip, port)
                        if result !=None:
                            self.outqueue.put(result)
                        self.queue.task_done()



#queue to fetch work from 
queue = Queue.Queue()
outqueue = Queue.Queue()

for i in range(10):
	#print "Creating WorkerThread : %d" %i

	#feed the queue to the Workerthread in order the threads know on what they 'll be working on
	worker = WorkerThread(queue, outqueue)
	worker.setDaemon(True)
	worker.start()
	#print "WorkerThread %d Created!"%i


for j in range(1024):
	queue.put(j)

queue.join()
print "All ports scanned"

for elem in list(outqueue.queue):
    print elem


