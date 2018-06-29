'''Dados dois números inteiros positivos, determinar o 
máximo divisor comum entre eles usando
o algoritmo de Euclides.'''

print("Calculo do MDC usando o Algoritmo de Euclides")

dividendo=int(input("Digite o maior numero: "))
divisor=int(input("Digite o menor numero: "))
resto=dividendo

while resto!=0:
	resto=dividendo%divisor
	if(resto!=0):
		dividendo=divisor
		divisor=resto

print(str(divisor))