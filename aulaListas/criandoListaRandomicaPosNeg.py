import random

def countNumber(l):
	''' the function count the numbers of negative and postivies
	numbers in list, that is pass for argument'''

	cont=0
	npositive=0
	nnegative=0

	while cont<len(l):
		if l[cont]>0:
			npositive=npositive+1
		else:
			if l[cont]<0:
				nnegative=nnegative+1
		cont=cont+1
	print("Number of positive numbers in list: "+str(npositive))
	print("Number of negative numbers in list: "+str(nnegative))
	
#create a empty list	
listnumber=[]
i=0
size=5

#add a random numbers in the list
while i<size:
	listnumber.append(random.randint(-100,100))
	i=i+1

countNumber(listnumber)

