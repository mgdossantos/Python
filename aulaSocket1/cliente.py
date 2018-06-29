import socket
import time 
HOST = '127.0.0.1' 
# Endereco IP do Servidor
PORT = 5000            
# Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Digite sair p/ finalizar\n')
msg = 'qqcoisa'
while msg!='sair':
    msg = input()
    udp.sendto(msg.encode('utf-8'), dest)
    print('recebendo')
    time.sleep(2)
    msgVolta,dest = udp.recvfrom(1024)
    print(msgVolta.decode('utf-8'))    
udp.close()