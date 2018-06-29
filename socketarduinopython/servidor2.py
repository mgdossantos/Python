import socket
import _thread
import os
import serial
import time
 
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

        if dados==b'3': 
            break

        else:
            if dados==b'2':
                print("Cliente para Arduino: ", dados.decode('utf-8'))
                conSerial.write(dados)
                time.sleep(1)
                mensagem = conSerial.readline()
                print("Arduino Diz: ", mensagem.decode('utf-8'))
                conexao.send(mensagem)

            else:
                print("Cliente para Arduino: ", dados.decode('utf-8'))
                conSerial.write(dados)
                mensagem = conSerial.readline()
                print("Arduino Diz: ", mensagem.decode('utf-8'))
 
    print('Cliente encerrou conexao', cliente)
    print("Terminando...")
    print("Fechando serial...")
    conSerial.close()
    print("Fechando conexao tcp...")
    tcpSOCKET.close()
    _thread.exit()
    sys.exit()
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexaoORIGEM = (HOST, PORTA)
tcpSOCKET.bind(conexaoORIGEM)
tcpSOCKET.listen(1)
 
while True:
 
    conexao, cliente = tcpSOCKET.accept()
    _thread.start_new_thread(conecta, tuple([conexao, cliente]))
 
