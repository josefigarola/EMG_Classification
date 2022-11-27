import datetime
import time
import select
import socket
import binascii
import ClassifyFingers as OT

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

hoh1 = HoH()
hoh1.connect()
UDP_IP = "127.0.0.1"
UDP_PORT = 2000
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if data == b'Selection: 1\n':
        hoh1.switch_demo_selec(6)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 2\n':
        hoh1.switch_demo_selec(5)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 3\n':
        hoh1.switch_demo_selec(4)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 4\n':
        hoh1.switch_demo_selec(3)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 5\n':
        hoh1.switch_demo_selec(2)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)
    elif data == b'Selection: 6\n':
        hoh1.switch_demo_selec(1)
        hoh1.switch_demo_mov(2)
        hoh1.switch_demo_mov(1)