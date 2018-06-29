#Listas + Funções
#Funções também podem tomar listas como entradas e realizar diversas operações nessas listas.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print(small)


#Escreva um função que conta quantas vezes a string "fizz" aparece em uma lista.

#Escreva uma função chamada fizz_count que toma uma lista x como entrada.
#Crie uma variável count para conter a contagem em andamento. Inicialize-a em zero.
#Para (for) cada item em x:, se (if) esse item for igual à string "fizz" então incremente a variável count.
#Depois do laço, retorne (return) a variável count.
#Por exemplo, fizz_count(["fizz","cat","fizz"]) deve retornar 2.