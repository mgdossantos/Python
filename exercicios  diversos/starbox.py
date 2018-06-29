def starbox(width, height):
    """imprime uma caixa feita e asteriscos.

    width: comprimento da caixa em caracteres, deve ser ao menos 2
    height: altura da caixa em linhas, deve ser ao menos 2
    """
    print("*" * width) # imprime a ponta superior da caixa

    # imprime os lados da caixa
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*") 

    print("*" * width) # imprime a ponta inferior da caixa

starbox(5,5)
starbox(3,2) 	