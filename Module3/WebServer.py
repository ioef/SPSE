#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer
import sys


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	
	def do_GET(self):
		
		if self.path =='/admin':
			self.wfile.write('This page is only for Admins')
			self.wfile.write(self.headers)
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


try:
	server = SocketServer.TCPServer(('',10001), HttpRequestHandler)
	server.serve_forever()

except KeyboardInterrupt:
	print "Terminating Server..."
	sys.exit()
