#!/usr/bin/env python

import immlib

DESC = 'FastLogHook Demo'
NAME = 'StrcpyFastLogHook'


def main(args):

    imm = immlib.Debugger()

    #create an object with the NAME provided
    injectHook = imm.getKnowledge(NAME)

    if injectHook:
        loggingResults = injectHook.getAllLog()
        imm.log(str(loggingResults))
        
        #Now we will parse the loggingResults
        (functionAddress, (esp, esp_4, esp_8)) = loggingResults[0]

        dataReceived = imm.readString(esp_8)

        imm.log(dataReceived)

        return '[+] Finished Fetching Results'



    #find the strcpy address
    functionToHook  = 'msvcrt.strcpy'
    
    #get the address of the provided function name
    functionAddress = imm.getAddress(functionToHook)

    #create a Fast LogHook 
    fastHook = immlib.FastLogHook(imm)
    
    fastHook.logFunction(functionAddress)

    fastHook.logBaseDisplacement('ESP', 0)
    fastHook.logBaseDisplacement('ESP', 4)
    fastHook.logBaseDisplacement('ESP', 8)

    fastHook.Hook()
        
    imm.addKnowledge(NAME, fastHook, force_add = 1)
  
    return "[+] Hook Added"


