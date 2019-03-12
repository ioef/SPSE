#!/usr/bin/env python

import pefile
import sys
import pprint


pe = pefile.PE('Server-Strcpy.exe')


for section in pe.sections:
    print section.Name
    print section.SizeOfRawData
    print '\n'
