'''Jogo de Craps. Faça um programa de implemente um jogo de 
Craps. O jogador lança um par de dados, obtendo um 
valor entre 2 e 12. '''

'''Se, na primeira jogada, você tirar 7
ou 11, você um "natural" e ganhou. '''

'''Se você tirar 2, 3 ou 12 na primeira jogada, 
isto é chamado de 
"craps" e você perdeu. '''

'''Se, na primeira jogada, 
você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até 
tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar 
este Ponto novamente.'''

import random

win=[7,11]
craps=[2,3,12]
jogada=[]
i=0

while i<2:
	jogada=random.randint(2,12)
	if jogada in win:
		print("vc eh um natural!! ganhou o jogo")
		break;
	if jogada in craps:
		print("craps!!! vc perdeu!!!")
		break;

	i=i+1

if dado1==7 or dado1==11 or dado2==7 or dado2==11:
	print("vc eh um natural!! ganhou o jogo")

if dado1==2 or dado1==3 or dado1==12 or dado2==2 or dado2==3 or dado2==12:
	print("craps!!! vc perdeu!!!")

