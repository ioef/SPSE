#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer
import CGIHTTPServer
import sys


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	
	def do_GET(self):
		
		if self.path =='/cgi-bin/':
			CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


try:
	server = SocketServer.TCPServer(('',10001), HttpRequestHandler)
	server.serve_forever()

except KeyboardInterrupt:
	print "Terminating Server..."
	sys.exit()
