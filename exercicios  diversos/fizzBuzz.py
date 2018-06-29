# entrada de dados: input
# conversao: int, float e str
# estrutura de selecao: if, if else, if encadeado
# concatenacao: +

# estrutura de repeticao 
cont=1
while(cont<20):
	if(cont%3==0) and (cont%5==0):
		print("FizzBuzz")
	else:
		if(cont%3==0):
			print("Fizz")
		else:
			if(cont%5==0):
				print("Buzz")
			else:
				print(cont)
	cont=cont+1