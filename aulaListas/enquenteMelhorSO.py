#codigo n finalizado
op=1

votos=[0,0,0,0,0,0]

while(op!=0):
	

	print('Qual o melhor Sistema Operacional para uso em servidores?')
	print('1- Windows Server')
	print('2- Unix')
	print('3- Linux')
	print('4- Netware')
	print('5- Mac OS')
	print('6- Outro')

	op=int(input())

	if op>6 or op<0:
		print('Opção invalida')
	else: 
		print('voto computado. obrigada!')
		if op==1:
			votos[0]=votos[0]+1
		if op==2:
			votos[1]=votos[1]+1
		if op==3:
			votos[2]=votos[2]+1
		if op==4:
			votos[3]=votos[3]+1
		if op==5:
			votos[4]=votos[4]+1
		if op==6:
			votos[5]=votos[5]+1
	
print(votos)

maior = max(votos)
print(maior)