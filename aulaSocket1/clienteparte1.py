import socket
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
rudp.close()