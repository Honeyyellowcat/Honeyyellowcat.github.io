import tkinter as tk
import serial
import time


def send_command():
    spd = speedEntry.get().zfill(3)
    dir = directionEntry.get()
    dir = (0 if dir == 'CW' else 1)
    rev = revEntry.get().zfill(3)
    cmd = str(dir) + ';' + rev + ';' + spd
    print cmd
    ser = serial.Serial('COM4', 9600, timeout=0,
                        parity=serial.PARITY_NONE, rtscts=0)
    time.sleep(2)
    ser.write(cmd.encode())
    ser.close()


def emergency_stop():
    ser = serial.Serial('COM4', 9600, timeout=0,
                        parity=serial.PARITY_NONE, rtscts=0)
    time.sleep(2)
    cmd = '0;000;000'
    ser.write(cmd.encode())
    ser.close()


root = tk.Tk()
root.title('Stepper Motor Control GUI')
root.geometry('400x100')
root.minsize(400, 100)
root.maxsize(400, 100)
speedLabel = tk.Label(root, text='Speed')
speedEntry = tk.Entry(root)
speedEntry.insert(0, '100')
speedLabelComment = tk.Label(root, text='1..100 %')
directionLabel = tk.Label(root, text='Direction')
directionEntry = tk.Entry(root)
directionEntry.insert(0, 'CW')
directionLabelComment = tk.Label(root, text='CW/CCW')
revLabel = tk.Label(root, text='Revolutions')
revEntry = tk.Entry(root)
revEntry.insert(0, '1')
revLabelComment = tk.Label(root, text='0..100 revs')
sendCommandButton = tk.Button(root, text='Send Command',
                              command=send_command)
sendCommandButton.grid(row=3, column=1)
emergencyStop = tk.Button(root, text='STOP!', command=emergency_stop)
emergencyStop.grid(row=3, column=2)
speedLabel.grid(row=0, column=0)
speedEntry.grid(row=0, column=1)
speedLabelComment.grid(row=0, column=2)
directionLabel.grid(row=1, column=0)
directionEntry.grid(row=1, column=1)
directionLabelComment.grid(row=1, column=2)
revLabel.grid(row=2, column=0)
revEntry.grid(row=2, column=1)
revLabelComment.grid(row=2, column=2)
root.mainloop()