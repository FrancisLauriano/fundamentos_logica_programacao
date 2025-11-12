def contido(lista_1: list, lista_2: list):
    if len(lista_1) > len(lista_2):
        return "Não está contido"
    else:
        inicio = len(lista_2) - len(lista_1)

        contido = True

        num1 = map(lista_1).split()
        num2 = map(lista_2).split()

        for i in range(inicio, len(lista_2)):
            if num1[inicio + i] != num2[i]:
                contido = False
                break

    if contido:
        print('Está contido')
    else:
        print('não está ciontido')
        

# num1, num2 = map(str, input('Número: ').split())

print(contido([1,2,3], [5,4,1,2,3,6]))