
import socket
import os
import serial
 
HOST = '127.0.0.1'
PORTA = 7000
 
tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destinoCONEXAO = (HOST, PORTA)
tcpSOCKET.connect(destinoCONEXAO)
 
os.system("clear")
print("|====================================|")
print("|    Arduino na rede usando Python   |")
print("|====================================|")
print("| Digite SAIR para teminar a conexao |")
 
dados =input()
 
while dados != 'SAIR':
    tcpSOCKET.send (dados.encode('utf-8'))
    dados = input()
tcpSOCKET.close()
