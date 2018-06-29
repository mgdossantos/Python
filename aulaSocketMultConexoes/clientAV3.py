# coding=utf-8
"""cliente.py
Este script enviará um valor para o servidor.
Você pode executar este script em mais de um terminal para testar.
"""
# Importando os módulos necessários.
import socket
from struct import *

# Criando o objeto.
s = socket.socket()

# Coletando o nome da máquina.
# O servidor está rodando na mesma máquina então terá o mesmo nome.
host = socket.gethostname()

# Porta onde a conexão é realizada.
port = 12345

# Realizando a conexão.
s.connect((host, port))

# Enviando um valor ao servidor.
# s.send(bytes('Mensagem vinda do cliente para o servidor', 'utf-8'))
msg=input("digite seu voto: ")
s.send(msg.encode('ascii'))

# Exibindo a mensagem vinda do servidor.
print(s.recv(1024).decode('ascii'))

# Fechando a conexão.
s.close