#!/usr/bin/env python
#created by Dr_Ciphers
#This is the solution to the excersise concerning the writing of the Processes
#in a csv file using the Immunity Debugger libraries.

import immlib
import csv
  
DESC = 'A simple ps list script writing to csv'


def main(args):
    imm = immlib.Debugger()
        
    td = imm.createTable('SPSE Course', ['PID', 'Name', 'Path', 'Services'])
    psList = imm.ps()

    with open('C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands\psFile.csv', 'wb') as csvfile:
        fieldNames = ['PID', 'Name', 'Path', 'Services']
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
                                  
        for process in psList:
            td.add(0, [str(process[0]), process[1], process[2], str(process[3])])
            writer.writerow({'PID':str(process[0]), 'Name':process[1], 'Path':process[2], 'Services':str(process[3])})
                                                                                        
     return '[+] Finished creating file with the process List'
