# coding=utf-8
"""servidor.py
Este código ficará em looping aguardando a conexão
(envio de dados) dos clientes.
"""

# Importando os módulos necessários.
import socket
# Criando o objeto
s = socket.socket()

# Coletando o nome da máquina onde os script é executado.
host = socket.gethostname()

# Porta reversa para o serviço.
port = 12345

# Disponibilizando o host e a porta
s.bind((host, port))

# Definindo que são esperadas até 5 conexões.
s.listen(5)

# Contador/somatório.
valor = 0
while True:
    # Estabelecendo conexão com o cliente.
    # Repare que estou utilizando atribuição múltipla.
    c, addr = s.accept()

    # Exibindo no terminal os dados da conexão.
    print("Conexão realizada em:"+str(addr))

    # Coletando a informação vinda do cliente.
   
    # Enviando uma mensagem de resposta ao cliente.
    msg="Valor enviado ao servidor recebido com sucesso"
    c.send(msg.encode('ascii'))

    recebido=int(c.recv(1024).decode('ascii'))
    # Realizando a soma do valor recebido pelo cliente.
    valor += recebido

    # Exibindo uma mensagem do terminal do servidor.
    print("Valor enviado pelo cliente "+str(recebido)+" Soma =" +str(valor))

    # Fechando a conexão.
    c.close()