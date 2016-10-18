#!/usr/bin/env python

import urllib
import sys


def fileRetrieve(num_of_Blocks, block_size, file_size):
	percentage = float(num_of_Blocks * block_size * 100) / file_size
	sys.stdout.write("                       ")
	sys.stdout.write("\rDownloading Completed %.2f %%     " %percentage)
	sys.stdout.flush()


url="http://cdimage.debian.org/debian-cd/8.6.0/amd64/iso-cd/debian-8.6.0-amd64-CD-1.iso"


dowloadedFile = urllib.urlretrieve(url, 'debian.iso', reporthook=fileRetrieve)

print "Download of file debian.iso completed"
