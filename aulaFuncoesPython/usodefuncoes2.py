aluno1=[['A','A','B'],['B','B','C'],['B','B','C']]
aluno2=[['B','B','C'],['C','C','B'],['C','C','B']]
aluno3=[['C','C','B'], ['A','A','B'],['A','A','B']]

print("Aluno 1")
for nlinha in range(3):
	linha=""
	for ncoluna in range(3):
		linha=linha+" "+str(aluno1[nlinha][ncoluna])
	print(linha)

print("Aluno 2")
for nlinha in range(3):
	linha=""
	for ncoluna in range(3):
		linha=linha+" "+str(aluno2[nlinha][ncoluna])
	print(linha)

print("Aluno 3")
for nlinha in range(3):
	linha=""
	for ncoluna in range(3):
		linha=linha+" "+str(aluno3[nlinha][ncoluna])
	print(linha)	