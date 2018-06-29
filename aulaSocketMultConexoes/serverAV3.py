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

lista=[]
i=0
# Contador/somatório.
while i<23:
    lista.append(0)
    i=i+1

recebido=-1

while recebido!=0:
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

    lista[recebido-1]=lista[recebido-1]+1

    # Exibindo uma mensagem do terminal do servidor.
    print("Valor enviado pelo cliente "+str(recebido)+" Votos =" +str(lista[recebido-1]))

    # Fechando a conexão.
    c.close()

print(lista)