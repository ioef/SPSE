#!/usr/bin/env python

import os
import sys
import time



def fileinfo(name):
	
	with open(name) as f:
        	if "#!/usr/bin/env python" in f.readline():
	             	print ("Python script, ASCII text")
		elif "#!/bin/bash" in f.readline():
			print ("Bash script, ASCII text")

	info = os.stat(name)
	print("Filename: %s"%name)
	
	if (os.access(name,os.X_OK)):
		print "Filetype: Executable"

	print("File_uid: %s"%info.st_uid)
	print("File_gid: %s"%info.st_gid)
	print("Filesize: %s Bytes" %info.st_size)

	#retrieve, convert and print local last modification and access time
	mtimelocal = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_mtime))
	atimelocal = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_atime))

	print("Last Modified : %s" %mtimelocal)
	print("Last Accessed : %s" %atimelocal)
	

def main():
	filename = sys.argv[1]
	fileinfo(filename)

if __name__== "__main__":
	main()
