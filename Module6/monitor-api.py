#!/usr/bin/env python

from pydbg import *
from pydbg.defines import *

def send_bp(dbg):
    print "Send() Called!"
    
    print dbg.dump_context(dbg.context)
    
    return DBG_CONTINUE


dbg = pydbg()


for pid, name in dbg.enumerate_processes():
    if name == 'Server-Strcpy.exe':
        dbg.attach(pid)

#monitot the send API call
send_api_addr = dbg.func_resolve("ws2_32", "send")

#monitot the rcv API call
send_api_addr = dbg.func_resolve("ws2_32", "recv"

dbg.bp_set(send_api_addr, description='Send BP', handler=send_bp)

dbg.run()