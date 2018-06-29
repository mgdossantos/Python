import socket

HOST = ''
PORT = 57000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
arq = open('/home/tchellita/Documentos/aulaSocket1/enviandoArquivo.txt', 'w')

while 1:
    dados = conn.recv(1024)
    if not dados:
        break
    arq.write(dados.decode('utf-8'))

arq.close()
conn.close()