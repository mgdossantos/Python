'''Supondo que a população de um país A seja da ordem de 
80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja
200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e 
escreva o número de anos
necessários para que a população do país A ultrapasse ou 
iguale a população do país B,
mantidas as taxas de crescimento'''

#fazer as populações crescerem
#vamos ver em 5 anos

populacaoA=80000
populacaoB=200000

ano=1
while ano<=5:
	populacaoA=populacaoA+populacaoA*0.03
	populacaoB=populacaoB+populacaoA*0.015

	print("Ano "+str(ano)+" - Populacao A: "+str(populacaoA))
	print("Ano "+str(ano)+" - Populacao B: "+str(populacaoB))

	ano=ano+1
