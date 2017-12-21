#!usr/bin/env python

import immlib
from immlib import BpHook


class StrcpyBpHook(BpHook):

    def __init__(self):
        BpHook.__init__(self)

    def run(self, regs):

        imm = immlib.Debugger()
        imm.log('StrcpyBpHook Called!')

        eipOnStack = imm.readLong(regs['ESP'])
        strcpyFirstArg  = imm.readLong(regs['ESP'] + 4)
        strcpySecondArg = imm.readLong(regs['ESP'] + 8)

        imm.log('EIP on Stack: 0x%08x First Arg: 0x%08x Second Arg: 0x%08x' %(eipOnStack, strcpyFirstArg, strcpySecondArg))
        
        imm.log(receivedString)
        imm.log('Received String: %s with length %d' %(str(receivedString), len(receivedString)))


def main(args):
    imm = immlib.Debugger()

    #find strcpy address
    functiontoHook  = 'msvcrt.strcpy'
    functionAddress = imm.getAddress(functionToHook)
    
    #instantiating the BreakPoint Hook object
    newHook = StrcpyBpHook()

    #This actually creates a BreakPoint based on the provided function Name and Address
    newHook.add(functiontoHook, functionAddress) 

    imm.log('Hook for %s: 0x%08x added Succesfully!' %(functionToHook, functionAddress))

    return 'Hook Installed successfully.'

