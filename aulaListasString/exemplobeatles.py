beatles=["John Lennon","Paul McCartney","George Harrison", "Ringo Starr"]
instrumentos=["guitarra rítmica e vocal","baixo, piano e vocal","guitarra solo e vocal","bateria e vocal"]


for cantor in beatles:
	print(cantor)

for instrumento in instrumentos:
	print(instrumento)

i=0
while i< len(beatles):
	print(beatles[i]+":"+instrumentos[i])
	i=i+1