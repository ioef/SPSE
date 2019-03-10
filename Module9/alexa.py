#!/usr/bin/env python
import sys
import re
from bs4 import BeautifulSoup
import requests
import Queue
import threading

topDict = {}

class WorkerThread(threading.Thread):
    
    def __init__(self, queue, lock):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock

    def engine(self, site):
        try:
            self.lock.acquire()
            print "Checking robot.txt of site %s"%site
            self.lock.release()
            
            htmlRobots = requests.get(site, timeout=1)

            if htmlRobots.status_code == 200:
                lines = htmlRobots.text.split('\n')

                for line in lines:
                    if line.find('Disallow:') !=-1 and not line.find('.') !=-1:
                        line = line.strip()
                        if line in topDict: 
                            topDict[line] += 1
                        else: 
                            topDict[line] = 1 
        except:
            print "[-] Problem with site %s"%site
            print "[!!] Trying next site"

    def run(self):
       while True:
                site = self.queue.get()
                self.engine(site)
                self.queue.task_done()



def main():

    html = requests.get('https://www.alexa.com/topsites')

    if html.status_code == 200:
        soup=BeautifulSoup(html.text,"lxml")
        divs = soup.findAll('div', {"class":"td DescriptionCell"})

        siteList = []

        #get the actual link of a href
        for div in divs:
            hrefLink = div.find('a').text
            hrefLink = 'http://' + hrefLink.lower() + '/robots.txt'
            siteList.append(hrefLink)
 


    queue = Queue.Queue()
    lock = threading.Lock()

    for i in range(10):
        #print "Creating WorkerThread : %d" %i

        #feed the queue to the Workerthread in order the threads know on what they 'll be working on
        worker = WorkerThread(queue, lock)
        worker.setDaemon(True)
        worker.start()
        #print "WorkerThread %d Created!"%i


    topTenList = siteList[0:10]
    
    for j in topTenList:
        queue.put(j)

    queue.join()


    finalDict =  sorted(topDict.iteritems(), key=lambda x: x[1], reverse=True)[:40]

    print ("[+] Top 40 Robots.tx ================")
    for item in finalDict:
        print "%s %s"%(item[0],item[1])



if __name__ == "__main__":
    main()

