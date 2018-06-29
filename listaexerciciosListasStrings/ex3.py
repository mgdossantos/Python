'''Faça um programa que crie dois vetores com 10 
elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão
 ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três
 vetores.'''

import random

A=[]
B=[]
C=[]

for i in range(10):
	valor=random.randint(1,100)
	A.append(valor)
	valor=random.randint(1,100)
	B.append(valor)
	C.append(A[i])
	C.append(B[i])

print(A)
print(B)
print(C)
