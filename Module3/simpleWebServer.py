#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer

server = SocketServer.TCPServer(('',10001), SimpleHTTPServer.SimpleHTTPRequestHandler)
server.serve_forever()
