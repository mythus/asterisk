#!/usr/bin/env python

import os
import sys
import subprocess
import pynagios
        
def ast_peer_status():
                
        '''Get current active sip peers accoring to asterisk'''
        astCmd=['asterisk' , '-rx' , 'sip show peers']
        try:
                astPipe = subprocess.Popen(     astCmd, 
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE  )
                # astStdout , astSdterr = astPipe.communicate()
                
        if astStderr :

            print astStderr , "LALALAL"
      #      raise IOError("Asterisk command returned error, astStderr")
    except Exception as e:
        print type(e),e.message
        print("Can not execute command. Check path and arguments") 
        return pynagios.Response(pynagios.UNKNOWN,'Can not execute asterisk command') 
    #print astStdout

if __name__ == '__main__':
    ast_peer_status()

