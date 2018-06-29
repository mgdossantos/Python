import socket                                         
import random


# a funcao gethostname retorna o nome da maquina
#host = ''socket.gethostname()                          
host=''
port = 9999
addr=(host,port)                                      

# criando o socket TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#Essa linha serve para zerar o TIME_WAIT do Socket
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind to the port
serversocket.bind(addr)                                  

# limite de conexoes	
serversocket.listen(5)                                           
msgclient='teste'

#estabelece conexao
clientsocket,client = serversocket.accept()
print("Conexao com: " + str(client))

drawNumber=random.randint(1,100)
print(drawNumber)
while msgclient!='0':
	      
	receive=clientsocket.recv(1024)
	msgclient=str(receive.decode('ascii'))
	print("Mensagem recebida: "+msgclient)
	if msgclient=='0':
		break
	else:
		choice=int(receive.decode('ascii'))
		if choice==drawNumber:
			msg="vc acertou o numero!!!"
		else:
			if choice<drawNumber:
				msg="tente um numero maior"
			else:
				msg="tente um numero menor"
	
	clientsocket.send(msg.encode('ascii'))

clientsocket.close()


 	