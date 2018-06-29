from random import randint
numerosecreto=randint(1,20)
chute=0
tentativa=0
while (tentativa<5) and (chute!=numerosecreto):
	chute=int(input("Digite seu chute: "))
	if(chute==numerosecreto):
		print("vc acertou")
	else:
		print("vc errou!!")
		if(chute>numerosecreto):
			print("vc digitou um numero muito grande !!!")
		else:
			print("vc digitou um numero muito pequeno !!!")
	tentativa=tentativa+1

print("fim do jogo")
if numerosecreto!=chute:
	print("o numero sorteado era "+str(numerosecreto))