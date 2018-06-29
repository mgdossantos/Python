'''Reverso do número. Faça uma função que retorne o reverso 
de um número inteiro informado. Por exemplo: 127 -> 721.'''


numero=(input("blablabla: "))
saida=""
i=len(numero)-1
while i>=0:
	saida= saida+numero[i] 
	i=i-1

print(saida)

saida2= numero[::-1]
print(saida2)