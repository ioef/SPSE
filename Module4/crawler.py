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
#import MySQLdb



MAX_DEPTH = 1 


#create the class that will handle the MySQL Object
#This class handles the mysql connection
class MySQLDB:
    def __init__(self, host, db, port, user, passwd):
        self.hostname = host
        self.port     = port
        self.df       = db
        self.user     = user
        self.passwd   = passwd


class crawlEngine(threading.Thread):
      def __init__(self, queue, base_url, max_depth, mysqlConnection):
          threading.Thread.__init__(self)
          self.queue           = queue 
          self.base_url        = base_url
          self.max_depth       = max_depth
          self.mysqlConnection = mysqlConnection


      def run(self):
          while True:
              pass

      def openurl(self):
          req = urllib2.Request(self.base_url)
          req.add_header('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0')
          resp = urllib2.urlopen(req)
          html = resp.read()
        
          return html  

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
    url = "https://www.google.com"

    crawler = crawlEngine(1, url, 0, 0)
    
    linkList = []
    
    html = crawler.openurl()
    linkList = crawler.get_links(html) 
    
    for link in linkList:
        print link


if __name__ == "__main__":
    main()
