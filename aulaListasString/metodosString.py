palavra='arquivo.py'

if palavra.startswith('M'):
	print("palavra começa com M")

if palavra.endswith('py')==False:
	print("palavra n termina com py")

resposta=input("resposta: ")
resposta.lower()

if resposta in 'sim, não, yes, no':
	print("resposta valida")


str1 = "programação de redes eh dificil!!!"
str2 = "des"

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 15))

print(str1.replace('dificil','trabalhoso'))

print(str1.split())
data='05/03/1984'
print(data.split('/'))

