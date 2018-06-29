import serial
import time
import tkinter as tk


def led_on():
     arduinoData.write(b'1')


def led_off():
     arduinoData.write(b'0')


led_control_window= tk.Tk()
btn=tk.Button(led_control_window,text="led on",command=led_on)
btn2=tk.Button(led_control_window,text="led off",command=led_off)
btn.pack()
btn2.pack()
arduinoData = serial.Serial('/dev/ttyACM0',9600)
led_control_window.mainloop()