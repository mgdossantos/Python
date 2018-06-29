listaip1=[]
ip= input('digite o ip: ')
listaip1=ip.split('.')
print(listaip1)

listaip=[]
i=0
while i<len(listaip1):
	listaip.append(int(listaip1[i]))
	i=i+1

if listaip[0]<=127:
	print("Classe A")
	print("ENDERECO DE REDE: "+ str(listaip[0])+".0.0.0")
	print("ENDERECO DE BROADCAST: "+ str(listaip[0])+".255.255.255")
else:
	if(listaip[0]==128 or listaip[0]<=191 and listaip[1]<=255):
		print("Classe B")
		print("ENDERECO DE REDE: "+ str(listaip[0])+"."+str(listaip[1])+".0.0")
		print("ENDERECO DE BROADCAST: "+ str(listaip[0])+"."+str(listaip[1])+".255.255")
	else:
		if(listaip[0]==192 or listaip[0]==223 and listaip[1]==255 and listaip[2]==255):
			print("Classe C")
			print("ENDERECO DE REDE: "+ str(listaip[0])+"."+str(listaip[1])+"."+str(listaip[2])+".0")
		print("ENDERECO DE BROADCAST: "+ str(listaip[0])+"."+str(listaip[1])+"."+str(listaip[2])+".255")