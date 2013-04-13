#!/usr/bin/env python

import re
import pynagios
        
class CheckCahnnel(pynagios.Plugin):
        
        channel = make_option("--check-channel", dest="channel", type="string")
        channelsDict = {
                        'dahdi' : ast_dahdi_status
                        'sip'   : ast_sip_status
                        'iax2'  ; ast_iax2_status
                        }
        
def ast_cmd_exec(astCmd):
                
        '''Exec the command and handle the exceptions'''
        if tech == 'sip'
                astCmd=['asterisk' , '-rx' , 'sip show peers']
        elif tech == 'dahdi'
                astCmd=['asterisk' , '-rx' , 'dahdi show status']
                
        try:
                astPipe = subprocess.Popen(     astCmd, 
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE  )
                astStdout , astSdterr = astPipe.communicate()
        except OSError as detail:
		pynagios.Response(pynagios.CRITICAL, "Check failed, check path: %s" % detail ).exit()
	except ValueError as detail:
		pynagios.Response(pynagios.CRITICAL, "Check failed, check Popen parameters: %s" % detail ).exit()
	except CalledProcessError as detail:
		pynagios.Response(pynagios.CRITICAL, "Check failed, asterisk exited with error: %s" % detail ).exit()

        if astStderr :
                pynagios.Response(pynagios.CRITICAL, "Check failed: %s" % astStderr).exit()
        
        
        return astStdout

def ast_sip_status(name)

        '''Check sip peer status and return rtt to the peer'''
        astCmd = ['asterisk' , '-rx' , 'sip show peer', name]
        astOut = ast_cmd_exec(astCmd)
        if re.search(r'Peer .* not found', astOut):
                pynagios.Response(pynagios.CRITICAL, "Check failed: %s" % astPut).exit()
                
        status = re.saerch(r'\s*Status\s*:.*', astOut).split(':').[1]
        
        if re.search(r'OK', status):
                qos = re.search(r'\((\d+)\s\w+\)', status).group(1)
                status = 'OK'
        else:
                pynagios.Response(pynagios.CRITICAL, "Peer unreachable, or qualify is off: %s" % status).exit()
        
        return status, qos

def ast_iax2_status(name)

        '''Check iax2 peer status and return rtt to the peer. For now it's like the sip check'''
        astCmd = ['asterisk' , '-rx' , 'iax2 show peer', name]
        astOut = ast_cmd_exec(astCmd)
        if re.search(r'Peer .* not found', astOut):
                pynagios.Response(pynagios.CRITICAL, "Check failed: %s" % astPut).exit()
                
        status = re.saerch(r'\s*Status\s*:.*', astOut).split(':').[1]
        
        if re.search(r'OK', status):
                qos = re.search(r'\((\d+)\s\w+\)', status).group(1)
                status = 'OK'
        else:
                pynagios.Response(pynagios.CRITICAL, "Peer unreachable, or qualify is off: %s" % status).exit()
        
        return status, qos
        
def ast_dahdi_status(description)
        '''Search dahdi car status by a description'''
        astCmd = ['asterisk' , '-rx' , 'dahdi show status']
        astOut =  ast_cmd_exec(astCmd)
        regexp = re.compile( re.escape(description) + r'.*\s+([A-Z]+)\s+\d+\s+\d+\s+(\d+)')
        status = None
        for card in astOut.split('\n'):
                if regexp.search(card):
                        status, crc4 = regexp.search(card).group(1,2)
        
        if status:
                return status , crc4
        else:
                pynagios.Response(pynagios.CRITICAL, "Dahdi chennel with this description not found").exit()
                
        
if __name__ == '__main__':
    ast_peer_status()

