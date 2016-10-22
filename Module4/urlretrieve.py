#!/usr/bin/env python

import urllib
import sys
import urlparse


def fileRetrieve(num_of_Blocks, block_size, file_size):
	percentage = float(num_of_Blocks * block_size * 100) / file_size
	sys.stdout.write("                       ")
	sys.stdout.write("\rDownloading Completed %.2f %%     " %percentage)
	sys.stdout.flush()

if len(sys.argv) != 2:
	print "usage ./urlretrieve.py http://fileurl.zip"
	sys.exit(0)

url= sys.argv[1]
#url="http://cdimage.debian.org/debian-cd/8.6.0/amd64/iso-cd/debian-8.6.0-amd64-CD-1.iso"


split = urlparse.urlsplit(url)
filename = split.path.split("/")[-1]


print "Downloading file %s" %filename

dowloadedFile = urllib.urlretrieve(url, filename, reporthook=fileRetrieve)

print "Downloading Completed"
