letras=[]
i=1

while i<=10:
	letras.append(input("Letra: "))
	i=i+1

i=0
cont=0

while i<=9:
	if letras[i] not in 'aeiou':
		cont=cont+1
	else:
		letras[i]="*"

	i=i+1

print("Numero de consoantes: "+ str(cont))
print(letras)
#e o numero de vogais??
