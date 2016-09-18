#!/usr/bin/env python

import threading
import Queue
import time 


class WorkerThread(threading.Thread):
	
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		print "In WorkerThread"
	
		step = 0
		while True:
			counter = self.queue.get()
			print "Ordered to sleep for %d seconds!" %counter
			time.sleep(counter)
			print "Finished Sleeping for %d seconds"%counter
			self.queue.task_done()



#queue to fetch work from 
queue = Queue.Queue()

for i in range(10):
	print "Creating WorkerThread : %d" %i

	#feed the queue to the Workerthread in order the threads know on what they 'll be working on
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "WorkerThread %d Created!"%i


for j in range(10):
	queue.put(j)

queue.join()
print "All tasks are over!"


