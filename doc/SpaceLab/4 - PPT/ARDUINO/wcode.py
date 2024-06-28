import serial.tools.list_ports
import pyfirmata
import time
import sys

#Important! For code to function properly, make sure motor driver + ports are plugged into Arduino 5V
#and motor driver - ports are plugged into Arduino digital pins defined below

#Define pin numbers
pulPin=2
dirPin=3
enPin=4

def get_ports():
    ports=serial.tools.list_ports.comports()
    return ports

def findArduino(portsFound):
    commPort = None
    for port in portsFound:
        if 'COM3' in port.device:
            commPort = port.device
            break
    return commPort


def stepX(steps):
    for i in range(0,steps):
        board.digital[pulPin].write(1)
        time.sleep(1e-3)
        board.digital[pulPin].write(0)
        time.sleep(1e-3)


foundPorts=get_ports()
connectPort=findArduino(foundPorts)

if connectPort != 'None':
    #ser=serial.Serial(connectPort, baudrate=9600, timeout=1)
    board=pyfirmata.Arduino(connectPort)
    print('Connected to '+connectPort)
else:
    print('Connection Issue!')
    sys.exit()

board.digital[enPin].write(1) #enable motor
board.digital[dirPin].write(0) #set motor direction. 1 is , 0 is 

stepX(1000)