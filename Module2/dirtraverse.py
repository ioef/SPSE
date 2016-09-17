#!/usr/bin/env python

import os


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

	traverseDir("/home/jeff/Downloads")


if __name__ == "__main__":
	main()

