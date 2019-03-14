#!/usr/bin/env python

from pydbg import *
from pydbg.defines import *
import sys
import utils

def detect_overflow(dbg) :

    if dbg.dbg.u.Exception.dwFirstChance:
        return DBG_EXCEPTION_NOT_HANDLED

    print "Access Violation Happened!"
    
    print "EIP: %0X"%dbg.Context.Eip

    # crash binning
    
    crash_info = utils.crash_binning.crash_binning()
    crash_info.record_crash(dbg)
    print crash_info.crash_synopsis()

    return DBG_EXCEPTION_NOT_HANDLED

dbg = pydbg()
dbg.load("Server-Strcpy.exe")


dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, detect_overflow)

dbg.run()
