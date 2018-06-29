disciplinas = [ "Programacao para Redes", "Organização de Computadores"," Redes I"]

print(disciplinas[0])

print(disciplinas[1])

print(disciplinas[2])

disciplinas.append("Laboratório 1")

print(disciplinas[3])

conceitos=[]
i=0

while i< len(disciplinas):

	conceitos.append(input("Digite o conceito da disciplina "+ disciplinas[i]+": "))
	i=i+1

print(disciplinas)
print(conceitos)

