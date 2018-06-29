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
msgserverdecode=''
while msg!='0':
	if msgserverdecode=="vc acertou o numero!!!":
		msg='0'
	else:
		msg=input("Qual seu chute?")
	
	socketclient.send(msg.encode('ascii'))
	
	if msg=='0':
		break
	# Receive no more than 1024 bytes
	time.sleep(1)
	msgserver = socketclient.recv(1024)
	msgserverdecode=msgserver.decode('ascii')                                     
	print (msgserverdecode)

socketclient.close()