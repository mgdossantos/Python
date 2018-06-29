valorDesejado=int(input("Qual valor vc deseja sacar? "))
nota10=0
nota100=0
nota50=0
nota20=0


if valorDesejado%10==0:
	while valorDesejado>0:
		if valorDesejado>=100:
			nota100=int(valorDesejado/100)
			resto=valorDesejado%100
		else:
			if valorDesejado>=50:
				nota50=int(resto/50)
				resto=resto%50
			else:
				if valorDesejado >= 20:
					nota20=int(resto/20)
					resto=resto%20
				else:
					nota10=int(resto/10)
					resto=resto%10
		valorDesejado=resto	
	print("Vc receberah "+ str(nota100)+ " notas de 100!!")
	print("Vc receberah  "+ str(nota50)+ " notas de 50!!")
	print("Vc receberah  "+ str(nota20)+ " notas de 20!!")
	print("Vc receberah  "+ str(nota10)+ " notas de 10!!")
else:
	print("Esse valor naum pode ser sacado nesse caixa")
