import random


def criaLista(tam):
	lista=[]
	for i in range(tamanho):
		valor=random.randint(1,10)
		lista.append(valor)
	return lista, max(lista),min(lista)


tamanho=int(input("Qual o tamanho da lista? "))
l, maior, menor=criaLista(tamanho)

print(l)
print("Maior: "+ str(maior))
print("Menor: "+ str(menor))

