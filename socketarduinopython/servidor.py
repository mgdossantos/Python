import socket
import _thread
import os
import serial
 
HOST = ''
PORTA = 7000
PORTA_SERIAL = '/dev/ttyACM0'
BAUD_RATE = 9600
 
conSerial = serial.Serial(PORTA_SERIAL, BAUD_RATE)
os.system("clear")
 
def conecta(conexao, cliente):
 
    print("IP conectado | Porta",   cliente)
 
    while True:
        dados = conexao.recv(1024)

        if not dados: break
        print("Cliente para Arduino: ", dados.decode('utf-8'))
        conSerial.write(dados)
        mensagem = conSerial.readline()
        print("Arduino Diz: ", mensagem.decode('utf-8'))
 
    print('Cliente encerrou conexao', cliente)
    print("Terminando...")
    conSerial.close()
    conexao.close()
    thread.exit()
    sys.exit()
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexaoORIGEM = (HOST, PORTA)
tcpSOCKET.bind(conexaoORIGEM)
tcpSOCKET.listen(1)
 
while True:
 
    conexao, cliente = tcpSOCKET.accept()
    _thread.start_new_thread(conecta, tuple([conexao, cliente]))
 
tcpSOCKET.close()