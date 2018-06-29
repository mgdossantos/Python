import socket
import time


# get local machine name
host = input("Digite o ip da maquina p/ conexao: ")                         
port = 9999
addr=(host,port)
# create a socket object
socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connection to hostname on the port.
socketclient.connect(addr)
msg='teste'
while msg!='0':
	msg=input("Digite a mensagem que deseja enviar para o servidor: ")
	socketclient.send(msg.encode('ascii'))
	if msg=='0':
		break
	# Receive no more than 1024 bytes
	time.sleep(5)
	msgserver = socketclient.recv(1024)                                     
	print (msgserver.decode('ascii'))

socketclient.close()