'''Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra 
o maior e o menor valor, sem usar
as funções max e min.'''

import random

lista=[]


for i in range(10):
	valor=random.randint(1,100)
	lista.append(valor)

maior=lista[0]
menor=lista[0]
i=0
while i < len(lista):
	if lista[i]> maior:
		maior=lista[i]
	if lista[i] < menor:
		menor=lista[i]

	i=i+1

print(lista)
print("Maior e menor sem usar as funcoes prontas!!!")
print("Maior: "+str(maior))
print("Menor: "+str(menor))

print("Maior e menor usando as funcoes prontas!!!")
print("Maior: "+str(max(lista)))
print("Menor: "+str(min(lista)))


