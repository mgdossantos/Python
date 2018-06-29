'''A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21,
34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; 
a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia 
um número inteiro calcule o seu número
de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.'''

primeiro=1
segundo=1

n=int(input("De quem vc deseja saber o numero de Fibonacci? "))
sequencia= str(primeiro)+ " - "+ str(segundo)

cont=2
while cont<n:
	termo=primeiro+segundo
	sequencia=sequencia+" - "+str(termo)
	primeiro=segundo
	segundo=termo
	cont=cont+1

print(sequencia)