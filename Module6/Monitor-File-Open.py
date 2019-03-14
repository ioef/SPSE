#!/usr/bin/env python

from pydbg import *
from pydbg.defines import *
import sys
import struct 

def CreateFile_breakpoint_callback(dbg) :

    pointer_on_stack = dbg.read_process_memory(dbg.context.Esp + 0x04, 4)
    unpacked_pointer = struct.unpack("<L", pointer_on_stack)[0]
    filename = dbg.smart_dereference(unpacked_pointer, True)

    print "Filename: %s" %filename
    return DBG_CONTINUE


dbg = pydbg()

dbg.attach(int(sys.argv[1]))

# find the address to set the breakpoint

bp_1 = dbg.func_resolve_debuggee("kernel32.dll", "CreateFileA")
bp_2 = dbg.func_resolve_debuggee("kernel32.dll", "CreateFileW")


dbg.bp_set(bp_1, description = "Create File Description", handler = CreateFile_breakpoint_callback)
dbg.bp_set(bp_2, description = "Create File Description 2", handler = CreateFile_breakpoint_callback)

dbg.debug_event_loop()


