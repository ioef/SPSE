#!/usr/bin/env python

import signal

timer = 2


def alarm_handler(signum, frame):
	exit(0)

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(timer)

while True:
	pass


