#!/usr/bin/env python

import os
import sys

def traverseDir(dirname):

	for currentDir, subDir, files in os.walk(dirname):
		level = currentDir.replace(dirname, '').count('/')
		indent = '-' * level * 4
	
		relpath = '{}{}/'.format(indent, os.path.basename(currentDir))
 
		print(relpath)

		subindent = '-' * 4 * (level + 1)

		for filename in files:
			if level == 0:
				print '{}{}'.format(indent, filename)
			else:
				print '{}{}'.format(subindent, filename)

def main():

	try:	
		directory = sys.argv[1]
		traverseDir(directory)
	except:
		print "Wrong Arguments! Please provide a path"


if __name__ == "__main__":
	main()

