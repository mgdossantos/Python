'''Socket: imagine socket como uma forma de comunicacao 
entre processos (programas em execucao). Socket são canais  
e comunicacao bidirecionais e podem prover comunicação entre
rocessos que etão rodando na mesma máquina ou em máquinas 
diferentes.

Existem sockets TCP, UDP ou sockets Unix. Cada um deles 
possui uma biblioteca (cjt de funcoes) que especificam o 
seu comportamento.'''

'''como criar um socket'''
'''s = socket.socket (socket_family, socket_type, protocol=0)'''

'''socket_family: qual a familia do socket: AF_UNIX or AF_INET'''
'''socket_type: tipo SOCK_STREAM or SOCK_DGRAM.'''
'''protocol: protocolo, por padrão é 0.'''

'''Para rodar nosso exemplos:
- abra um terminal e rode o servidor
- abra um novo terminal e rode o cliente
- dica: abra duas janelas separadas que fica 
melhor para avaliar a saida de dados'''