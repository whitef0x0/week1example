import sys
import serial
import re

class UnexpectedResult(Exception):
    pass


class IridiumSBD(object):
    BAUD_RATE = 19200
    TIMEOUT = 10
    
    def __init__(self, port_name):
        self.port_name = port_name
        
    def connect(self):
        self.port = serial.Serial(self.port_name, baudrate=self.BAUD_RATE,timeout=self.TIMEOUT)
        
    def connect_to_network(self):
       self.send_command("+CIER=1,1,0,0",'+CIEV:0,' ) #question about regexp here
        
    def set_echo(self, on):
        self.send_command('E', int(bool(on)))
        
    def send_command(self, command_name, end_reg_exp='OK\r', option=''):
        self.port.write('AT' + command_name + str(option) + '\r')
        data = ''
        while not data.endswith(end_reg_exp):
            data += self.port.read(1)
        return data
                    
    def get_system_time(self):
        data = self.send_command("+CCLK?")
        matcher = re.compile('CCLK:(\d+)\/(/d+)\/(/d+),(\d+):(\d+):(\d+)')
        parsed_data = matcher.findall(data)
        if len(parsed_data) == 1:
            return parsed_data[0] #question here as well
        else:
            print(parsed_data)
            #raise UnexpectedResult()
        
"""  def start_SBD_session(self):
        data = self.send_command("+SBDIXA")
        matcher = re.compile('+SBDIX: (\d+), (\d+), (\d+), (\d+), (\d+), (\d+)')
        parsed_data = matcher.findall(data)
        
        status = parsed_data[1]
        # a bunch of other variables that I need to look up
        
        if status <= 4:
            print"MO message transferred succesfully"
        else if status == 18:
            print"MO message failed, radio failure"
        else if status == 32:
            print"MO message failed, network failure"
        else:
            print("MO message failed, error"+status)
"""
"""    def send_SBD_message(self,message="AT+SBDD0"):
        data = self.send_command("AT+SBDWT+"+message)
"""  
        
if __name__ == '__main__':
    sbd = IridiumSBD(sys.argv[1])
    sbd.connect()
    print(sbd.get_system_time())
    