#!/usr/bin/env python

import signal


def ctrl_handler(signum, frm):

	print "Haha! You cannot kill me!"


def main():

	print "Installing signal Handler"
	signal.signal(signal.SIGINT, ctrl_handler)

	print "Done!"
	
	while True:
		pass



if __name__=="__main__":
	main()
