#!/usr/bin/env python

import pefile
import sys

fileName = sys.argv[1]

pe = pefile.PE(fileName)

for item in pe.DIRECTORY_ENTRY_IMPORT:
        print "DLL File: %s"%item.dll.lower()
        print "Functions: "
        for import_fn in item.imports:
            print hex(import_fn.address), import_fn.name
        print '\n'
