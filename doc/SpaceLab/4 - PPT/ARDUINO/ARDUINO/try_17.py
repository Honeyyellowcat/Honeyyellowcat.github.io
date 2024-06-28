import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
board.digital[3].high(1)

try :
    while True :
        board.digital[2].write(1)
        time.sleep(1)
        board.digital[2].write(0)
        time.sleep(1)
except :
    board.exit()