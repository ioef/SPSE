#!/usr/bin/env python

import threading
import Queue
import time

class workerThread(threading.Thread):
    def __init__(self, queue, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock

    def do_work(self, item):
        #below you can call anycode you want
        #we have a basic task simulation example that executes in 0.1seconds
        time.sleep(0.1)
        #end of code
        with lock:
            print threading.current_thread().name, item


    def run(self):
        while True:
            item = queue.get()
            self.do_work(item)
            queue.task_done()


#create an empty queue
queue = Queue.Queue()
#create a lock for having serialized consolse output 
lock = threading.Lock()

#just get the current time in order to perform a subsctraction later
start = time.time()

#creation/preparation of the threads and their properties
for i in range(5):
    t = workerThread(queue, lock)
    t.setDaemon(True)
    t.start()

#put the items to the queue
queueSize = 10

for item in range(queueSize):
    queue.put(item)

#block until all items are completed
queue.join()

print ('Executed %s items in time: %s seconds' %(queueSize, time.time() - start))
print ('with single Threading this would take: %s seconds' %(queueSize * 0.1))
