#Iridium SBD Library

import sys
import serial



    DEFAULT_TIMEOUT = 60000
    SIMPLE_COMMAND_TIMEOUT = 2000
    TIMEOUT_FOREVER = -1
    port = serial.Serial(ttyUSB0#fjkelwjfel)
    bars = 0
    debug = 1
    class unsollicited:
        #a bunch of stuff
        
    
    
    def sbdring():
        #emit event
    
    #debug messages?
    def debug():
        if(debug):
            print(message)
     
            
    def areg(#line):
    
    
#function for sending SBD message 
    def sendBinaryMessage(message, callback, maxWait):
        
        if(message.length == 0):
            sendMessage(message,callback,maxWait)
            return
        
        #var buffer = (message instanaceof Buffer)?message:new Buffer(message);
        command = 'AT+SBDWB=' + len(buffer)
        
        #var ob = new Buffer(buffer.length+2);
        sum = 0
        for i in range(len(buffer)):
            ob[i] = buffer[i]
            sum += buffer[i]
            
        ob[len(buffer)+1]=#sum&0xff
        sum>>=8
        ob[len(buffer)]=sum&0xff
        
        AT(command, """READY""", ALL, """somesort of function""")
           # a whole bunch of things I don't understand
           
    def sendMessage(message,callback,maxWait):
        
        #if no message given
        command = message#some AT code
        
        #calls the AT function again
        
    binaryMode = false
    binaryBuffer = buffer(512)
    binaryBufferCounter = 0
            
     #binary mode function. Needed?   
        
        
    
    
    
    def AT(command, endregexp, keepregexp, datafunction, timeout):
        er = endregexp;
        kr = keepregexp
        if(tf)