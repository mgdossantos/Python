import socket
HOST = ''  
# Endereco IP do Servidor
PORT = 5000
# Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    msg= msg.decode('utf-8')
    print(cliente,msg)
    msg=msg.upper()
    udp.sendto(msg.encode('utf-8'),cliente)
udp.close()