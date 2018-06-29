'''Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os 
números pares na lista PAR e os números ímpares na lista IMPAR. 
Imprima as três listas.'''


lista=[]
listaPar=[]
listaImpar=[]

import random

lista=[]


for i in range(20):
	valor=random.randint(1,100)
	lista.append(valor)

i=0
while i < len(lista):
	if lista[i]%2==0: 
		listaPar.append(lista[i])
	else:
		listaImpar.append(lista[i])

	i=i+1


print(lista)
print(listaImpar)
print(listaPar)