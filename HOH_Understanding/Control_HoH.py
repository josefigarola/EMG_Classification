'''
    # a5 is the header -> always has to be 0xa5.
    # 1 byte for mask -> Change ROM and other parameters
    # 1 byte for command -> Which Fingers
    # 1 byte for inta -> leave as it is 00 for "dummy" purposes.
'''

import datetime
import time
import select
import socket
import binascii

band=0

class HoH():
    def __init__(self):
        self.s = socket.socket()
        self.s.settimeout(15)
        
    def switch_demo_mov(self,argument):
        arg = argument
        
        if arg == 1:
            print("GO")                     #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a5600000')
            time.sleep(4)
        elif arg == 2:
            print("RESET")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a5602000')
            time.sleep(4)

    def switch_demo_selec(self,movement):
        mov=movement
        if mov==1:
            print("Thumb")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9000')
        elif mov==2:
            print("Index")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f8800')
        elif mov==3:
            print("Middle")                 #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f8400')
        elif mov==4:
            print("Ring")                   #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f8200')
        elif mov==5:
            print("Little")                 #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f8100')
        elif mov==6:
            print("Hand")                   #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9f00')
            
    def switch_demo_joy(self,movement):
        mov=movement
        if mov==1:
            print("Thumb and Index")                    #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9800')
        elif mov==2:
            print("F**k")                    #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9b00')
        elif mov==3:
            print("Rock")               #---Commented for final version - print on
            # Comandos
            self.CSSend('a59f9600')
        elif mov==4:
            print("Peace n' love")               #---Commented for final version - print on
            # Comandos
            self.CSSend('a59f9300')
            
    def switch_demo_rehab (self,movement):
        mov=movement
        if mov==1:
            print("Thumb Up")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f8f00')
        elif mov==2:
            print("Index Up")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9700')
        elif mov==3:
            print("Middle Up")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9b00')
        elif mov==4:
            print("Ring Up")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9d00')
        elif mov==5:
            print("Pinky Up")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9e00')
            
    def switch_demo_rehab_seq(self,movement):
        mov=movement
        if mov==1: # Pinzas 1
            print("Sequence 1")                  #---Commented for final version - print on terminal
            #Comandos
            self.CSSend('a59f9100') # Thumb -> Pinky
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            
            # Comandos
            self.CSSend('a59f9200') # Thumb -> Ring
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            
            # Comandos
            self.CSSend('a59f9400') # Thumb -> Middle
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            
            # Comandos
            self.CSSend('a59f9800') # Thumb -> Index
            hoh1.switch_demo_mov(2)           

        if mov==2: # Pinzas 2 
            print("Sequence 2")  
            # Comandos
            self.CSSend('a59f9100') # Thumb -> Pinky
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            # Comandos
            self.CSSend('a59f9400') # Thumb -> middle
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            # Comandos
            self.CSSend('a59f9000') # just thumb
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            #C Comandos
            self.CSSend('a59f9800') # thumb -> index
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            # Comandos
            self.CSSend('a59f9200') # thumb -> ring
            hoh1.switch_demo_mov(2)
            hoh1.switch_demo_mov(1)
            # Comandos
            self.CSSend('a59f9000') # just thumnb
            
    def CSSend(self, hexstring):
        self.idleTime = 100
        if int(hexstring[0:2], 16) != 0xa5:
            return
        mask = int(hexstring[2:4], 16)
        cmd = int(hexstring[4:6], 16)
        inta = int(hexstring[6:8], 16)
        checksum = (mask + cmd + inta) % 256
        try:
            self.s.send(bytearray([0xa5]))

            self.s.send(bytearray([mask]))

            self.s.send(bytearray([cmd]))

            self.s.send(bytearray([inta]))

            self.s.send(bytearray([checksum]))

        except:
            print('Error in sending message')
        return

    def sendgo(self):
        self.CSSend('a5602000')

    def sendstop(self):
        self.CSSend('a5604000')

    def sendCali(self):
        self.CSSend('a5606000')

    def sendreset(self):
        self.CSSend('a5600000')
        
    def connect(self):
        global band
        HOST = input("Introduzca IP: ")     
        HOST = str(HOST).replace(' ', '')       
        self.s = socket.socket()
        self.s.settimeout(0.5)                  
        try:
            self.s.connect((HOST, 2000))
            print('Connected to HoH\nPlease wait while doing a test routine\n')
            #Movimientos iniciales
            self.switch_demo_selec(6)   #All hand
            self.s.settimeout(4)
            self.switch_demo_mov(1)     #Reset
            self.s.settimeout(4)
            self.switch_demo_mov(2)     #Go
            self.s.settimeout(4)
            self.switch_demo_mov(1)     #Reset
            band=1
        except:
            print("Something's wrong with connection to HOH [%s]" % HOST)   #---Commented for final version - print on terminal
            band=0
        if band==1: 
            print('\nYou can start BrainTec\n')
            self.switch_demo_selec(6)

''' Main Code '''
hoh1 = HoH()
hoh1.connect()
UDP_IP = "127.0.0.1"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# 192.168.137.21
while True:
    # Get data from the BCI
    #data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = b'Selection: 16\n' # Debugging purposes
    
    # Isolated Movement
    if data == b'Selection: 1\n': # Hand
        hoh1.switch_demo_selec(6) 
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 2\n': # Pinky
        hoh1.switch_demo_selec(5) 
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 3\n': # Eing
        hoh1.switch_demo_selec(4)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 4\n': # Middle
        hoh1.switch_demo_selec(3)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 5\n': # Index
        hoh1.switch_demo_selec(2)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 6\n': # Thumb
        hoh1.switch_demo_selec(1)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    
    # COMPOUND JOY MOVEMENTS
    elif data == b'Selection: 7\n': # Nice
        hoh1.switch_demo_joy(1)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 8\n': # F**k
        hoh1.switch_demo_joy(2)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 9\n': # Rock
        hoh1.switch_demo_joy(3)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 10\n': # Peace n' love
        hoh1.switch_demo_joy(4)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
        
    # COMPOUND REHAB MOVEMENTS
    elif data == b'Selection: 11\n': # Thumb Up
        hoh1.switch_demo_rehab(1)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 12\n': # Index Up
        hoh1.switch_demo_rehab(2)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 13\n': # Middle Up
        hoh1.switch_demo_rehab(3)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 14\n': # Ring Up
        hoh1.switch_demo_rehab(4)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 15\n': # Pinky Up
        hoh1.switch_demo_rehab(5)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
        
    # SEQUENCE REHAB MOVEMENTS
    elif data == b'Selection: 16\n': # Pinzas
        hoh1.switch_demo_rehab_seq(1) 
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 17\n': # Pinzas 2
        hoh1.switch_demo_rehab_seq(2) 
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)