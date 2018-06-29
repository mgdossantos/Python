#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

tamanho=0
nome=input("Digite seu nome: ")
tamanho=len(nome)
if(tamanho>3):
	print("nome válido")

idade=int(input("Digite sua idade: "))
if idade >0 and idade <150:
	print("idade válida")

salario= float(input("Digite seu salario"))
if salario>0:
	print("Salário válido")

sexo=input("Digite seu sexo: F - feminino /  M - masculino / O - outro")
sexo=sexo.upper()	
sexoCaractere=sexo[0]

if sexoCaractere=='F' or sexoCaractere=='M' or sexoCaractere=='O' :  
	print("Sexo válido")

estadoCivil=input("Digite seu estado civil: S - solteiro C - casado V - viuvo D - divorciado")
estadoCivil=estadoCivil.upper()
estadoCivilCaractere=estadoCivil[0]


if estadoCivilCaractere=='S' or estadoCivilCaractere=='C' or estadoCivilCaractere=='V' or estadoCivilCaractere=='D'  :  
	print("Estado Civil Válido")



