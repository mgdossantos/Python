'''Faça um programa que leia um nome de usuário e a 
sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.'''
import getpass

nome="programacao"
senha=nome

while (nome==senha):
	nome=input("Digite seu nome: ")
	senha=getpass.getpass("Digite sua senha: ")
	senha=senha.upper()
	nome=nome.upper()

	if nome==senha:
		print("Seu nome e sua senha naum podem ser iguais")

print("Dados salvos com sucesso!!")