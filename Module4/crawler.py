#!/usr/bin/env python
#created for Module 4.7, Attacking Web Applications
#This is actually a multithreaded webcrawler 
#that accepts as input a hostname of a target and a maximum number of depth for crawling
#It saves only the HTML pages and saves the structure on a DB Schema

#Before the very first execution the system shall have installed the mysql and a DB configured
#sudo mysql
#mysql> SHOW DATABASES;
#mysql> CREATE DATABASE spsedb;
#mysql> CREATE USER 'test'@'localhost' IDENTIFIED BY 'simplepass';
#mysql> USE spsedb;
#mysql> GRANT ALL ON spsedb.* TO 'test'@'localhost';
#mysql> quit;


import threading
from Queue import Queue
from optparse import OptionParser
from bs4 import BeautifulSoup
import urllib2
import sys
#import MySQLdb



#create the class that will handle the MySQL Object
#This class handles the mysql connection
class MySQLDB:
    #Class that is responsible for the connection data of the mysql
    def __init__(self, hostname, port, db, user, passwd):
        self.hostname = hostname
        self.port     = port
        self.db       = db
        self.user     = user
        self.passwd   = passwd


class crawlEngine(threading.Thread):
      def __init__(self, queue, base_url, max_depth, url_list, lock, mysqlConnection):
          threading.Thread.__init__(self)
          self.queue           = queue 
          self.base_url        = base_url
          self.base_domain     = self.getdomain(base_url)
          self.depth           = 0
          self.url_list        = url_list
          self.max_depth       = max_depth
          self.mysqlConnection = mysqlConnection
          self.lock            = lock

      def run(self):
          while True:
              url, self.depth = self.queue.get()
              current_domain  = self.getdomain(url)

              if self.base_domain != current_domain:
                  self.queue.task_done()
                  continue
              

              html = self.openurl(url)
              
              if html !=-1:
                  print "\r{0}Domain: {1} : depth: {2}".format('----'*self.depth, url, self.depth)
                  if self.depth < self.max_depth:
                      links = self.get_links(html)
                      for link in links:
                          self.addurltoList(link)
                  else:
                      self.queue.task_done()
                      continue


              self.queue.task_done()

      def openurl(self, url):
          try:
              req = urllib2.Request(url)
              req.add_header('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0')
              resp = urllib2.urlopen(req)
              if resp.code == 200:
                  html = resp.read()
                  return html  
              else:
                  return -1
          except:
              return -1


      def addurltoList(self, link):
          
          self.lock.acquire()
          if link not in self.url_list:
              self.url_list.append(link)
              self.queue.put((link, self.depth +1))
          self.lock.release()
 
      def getdomain(self, url):
          #extract the network location part e.g. the domain
          if url.startswith('http') or url.startswith('https'):
              domain = url.split('/')[2]
          else:
              domain = url.split('/')[0]

          return domain

      def get_links(self,html):
   
          bs = BeautifulSoup(html, 'lxml') 
          
          links = []
          for link in bs.find_all('a', href=True):
              if not link['href'].startswith('#'):
                  #if it is a relative path convert it to absolute
                  #and append in the links list
                  if link['href'][0] == '/': 
                      links.append(self.base_url + link['href'])                    
                 
                  #if it starts with http or https append the absolute
                  #path to the list. Ignore everything else like "javascript void(0) etc." 
                  if link['href'].startswith('http'):
                      links.append(link['href'])
     
          return links



def main():

    if len(sys.argv) !=2:
        sys.exit(-1)
    
    url = sys.argv[1]
    threads = 5

    #initialization of an empty Queue
    queue = Queue()
   
    queue.put((url,1))

    url_list = [] 
    max_depth = 5

    lock = threading.Lock()

    for i in xrange(threads):
        crawler = crawlEngine(queue, url, max_depth, url_list, lock, 0)
        crawler.setDaemon(True)
        crawler.start()

    queue.join()


if __name__ == "__main__":
    main()
