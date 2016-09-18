#!/usr/bin/env python

import threading
import Queue
import time 
from ftplib import FTP

class WorkerThread(threading.Thread):
	
	def __init__(self, queue,lock):
		threading.Thread.__init__(self)
		self.queue = queue
		self.lock = lock

	def run(self):
		print "In WorkerThread"
	
		step = 0
		while True:
			
			self.lock.acquire()
			#retrieve from the queue a single FTP Server IP
			ftpServerIP = self.queue.get()
			
			print "Scanning FTP Server at %s!" %ftpServerIP
			ftp = FTP(ftpServerIP)
			try:
				ftp.login()
				ftp.retrlines('LIST')
				ftp.close()
			except: 
				print "Permission Denied or other error occured!"

			print "Finished FTP Server at %s "%ftpServerIP
			time.sleep(1)
			self.queue.task_done()
			self.lock.release()


def main():

	noOfThreads = 10

	with open("ftpsites.txt","r") as f:
		ftpSites = f.readlines()


	
	#queue to fetch work from 
	queue = Queue.Queue()
	
	#create locks for the threads
	lock=threading.Lock()

	for i in range(noOfThreads):
		print "Creating WorkerThread : %d" %i

		#feed the queue to the Workerthread in order the threads know on what they 'll be working on
		worker = WorkerThread(queue,lock)
		worker.setDaemon(True)
		worker.start()
		print "WorkerThread %d Created!"%i

	
	#create a queue which includes all the ftpsites in the file 
	for ip in ftpSites:
		queue.put(ip)

	queue.join()
	print "All FTP sites scanned!"



if __name__=="__main__":
	main()
