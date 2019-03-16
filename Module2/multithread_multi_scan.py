#!/usr/bin/env python

import threading
from scapy.all import * 
import Queue
import time 

ip="192.168.1.12"

class WorkerThread(threading.Thread):
	
    def __init__(self, queue, outqueue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.outqueue = outqueue

    #General Info about TCP layer Flags
    #
    #	URG = 0x20
    #	ACK = 0x10
    #	PSH = 0x08
    #	RST = 0x04
    #	SYN = 0x02
    #	FIN = 0x01		

    def scannerSYN(self, ip, port):
	#SYN Scanning cases
	# Port is Open : 1) Client sends SYN Flag -> 2) Server Sends back SYN/ACK Flag <- 3) Cient Sends RST Flag ->
	# Port is Closed: 1) Client sends SYN Flag -> 2) Server Sends back RST Flag <-
	# Port is Filtered: 1) Client sends SYN Flag -> 2) Server Sends back ICMP Error <-		
        sport = RandShort()
        response = sr1(IP(dst=ip)/TCP(sport=sport,dport=port, flags="S"), verbose=False, timeout=.5)   
        if response !=None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                return "[+] PortNumber %s OPEN"%port
            elif response.haslayer(ICMP):            
                if (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
		            return "[+] PortNumber %s Filtered"%port
            #elif response[TCP].flags ==  0x14:
            #    return "[+] PortNumber %s is CLOSED"%port
        else:
            pass
		
    def scannerFINorXMAS(self, ip, port, t="XMAS"):
        #SYN Scanning cases
	# Port is Open or Filtered : 1) Client sends XMAS Flag -> 2) Server is not responding
	# Port is Closed: 1) Client sends XMAS Flag -> 2) Server Sends back RST Flag <-	
        sport = RandShort()
        try:
            if t=="XMAS":
                response = sr1(IP(dst=ip)/TCP(sport=sport,dport=port, flags="FPU"), verbose=False, timeout=.5)   			
            else:
                response = sr1(IP(dst=ip)/TCP(sport=sport,dport=port, flags="F"), verbose=False, timeout=.5)   			
	    
            if str(type(response)) == "<type 'NoneType'>":
	        return "[+] PortNumber %s OPEN"%port
            #elif response.haslayer(TCP):
	        #if response.getlayer(TCP).flags == 0x14:
		#    return "[+] PortNumber %s is CLOSED"%port
                #elif (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]): 
		#    return "[+] PortNumber %s Filtered"%port
        except Exception as e:
	    pass
		
    def run(self):
	    #print "In WorkerThread"
        step = 0
        while True:
            port = self.queue.get()
            result = self.scannerSYN(ip, port)
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
print "All ports 1024 scanned"

for elem in list(outqueue.queue):
    print elem


