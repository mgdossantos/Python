palavra=input("Digite uma palavra: ")

i=0
palavraNova=""

while i<len(palavra):
	if palavra[i] in 'aeiou':
		palavraNova=palavraNova+"*"
	else:
		palavraNova=palavraNova+palavra[i]
	i=i+1
	

print(palavra)
print(palavraNova)
