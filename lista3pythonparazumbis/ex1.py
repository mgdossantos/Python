"""Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário 
informe um valor válido."""


#pedir uma nota
nota= float(input("Digite uma nota: "))
#mensagem caso nota seja invalida
if(nota<0 or nota>10):
	print("Nota invalida")
