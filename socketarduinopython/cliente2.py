
import socket
import os
import serial
import time
import tkinter as tk

HOST = '127.0.0.1'
PORTA = 7000
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def led_on():
	dados=b'1'
	tcpSOCKET.send (dados)
    

def led_off():
	dados=b'0'
	tcpSOCKET.send (dados)


def obterleiturasensorLDR():
	dados=b'2'
	tcpSOCKET.send (dados)
	time.sleep(3)
	dados = tcpSOCKET.recv(1024)
	dados=dados.decode('utf-8')
	dadosf=str(dados)
	print(dadosf)
	dadosf.strip()
	sensor.set(dadosf)
	
def encerrar_conexao():
	dados=b'3'
	tcpSOCKET.send(dados)
	time.sleep(2)
	tcpSOCKET.close()


def iniciar_conexao():
	destinoCONEXAO = (HOST, PORTA)
	tcpSOCKET.connect(destinoCONEXAO)


dadosf=0
led_control_window= tk.Tk()
btn1=tk.Button(led_control_window,text="led on",command=led_on)
btn2=tk.Button(led_control_window,text="led off",command=led_off)
btn3=tk.Button(led_control_window,text="obter leitura do sensor de Luminosidade",command=obterleiturasensorLDR)
lbSensorLDR = tk.Label(led_control_window, text ='LUMINOSIDADE')
sensor = tk.StringVar()
sensor.set(dadosf)
w = tk.Label(led_control_window, textvariable =sensor)
btn4=tk.Button(led_control_window,text="iniciar conexao",command=iniciar_conexao)
btn5=tk.Button(led_control_window,text="encerrar conexao",command=encerrar_conexao)

btn1.pack()
btn2.pack()
btn3.pack()
lbSensorLDR.pack()
w.pack()
btn4.pack()
btn4.pack()
btn5.pack()

led_control_window.mainloop()

