# As listas podem ser com texto

cores=['vermelho', 'azul', 'verde']
print(cores[0]) 
print(len(cores))


#Ou podem ser com números

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
	sum += num
print(sum) 



#list.append(elem)
#list.insert(index, elem) 
#list.extend(list2)
#list.index(elem) 
#list.remove(elem) 
#list.sort()
#list.reverse()
#list.pop(index)


lista3 = ['marcela', 'fernando', 'marcelo']
lista3.append('fernanda')        
lista3.insert(0, 'bernardo')    
lista3.extend(['flavia', 'marcia']) 
print(list)  
print(lista3.index('marcela')) 

lista3.remove('marcela')  
print(lista3)        
print(lista3.pop(1))                  
print(lista3)  


lista = []          
lista.append('a')  
lista.append('b')
print(lista)



lista2 = ['a', 'b', 'c', 'd']
print(lista2[1:-1])   ## ['b', 'c']
lista2[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(lista2)         ## ['z', 'c', 'd']