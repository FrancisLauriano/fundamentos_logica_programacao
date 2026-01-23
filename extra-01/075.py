def maior_menor(numeros: tuple) -> str:
    # qtd_vezes = 0
    # for numero in numeros:
    #     if 9 == numero:
    #         qtd_vezes += 1

    if 9 not in numeros:
        qtd_vezes = f'Número 9 não está incluido na tupla'
    else:
        qtd_vezes = f'Número 9 aparece {numeros.count(9)} vezes'
    
    if 3 not in numeros:
        posicao_tres_primera_vez = f'Número 3 não está incluido na tupla'
    else:
        posicao_tres_primera_vez = f'O primeiro valor 3 aparece na posição {numeros.index(3)}'
        
    tupla_numeros_pares = ()
    for numero in numeros:
        if numero % 2 == 0:
            tupla_numeros_pares += (numero, )
        numeros_pares = f'Os valores pares são: {tupla_numeros_pares}'
    
    
    return f'{qtd_vezes}\n{posicao_tres_primera_vez}\n{numeros_pares}'
        


numeros = ()
for _ in range(4):
    numero = int(input('Digite um número: '))
    numeros += (numero, )

print(maior_menor(numeros))




