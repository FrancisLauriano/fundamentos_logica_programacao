# 2. Faça o algoritmo e o fluxograma que implementa a divisão inteira.

dividendo = int(input('Informe o dividendo: '))
divisor = int(input('Informe o divisor: '))

if divisor == 0:
    print(f'[ERRO] O divisor não pode ser zero!')
else:    
    inteiro = dividendo // divisor
    resto = dividendo % divisor

    print(f'O inteiro da divisão entre ${dividendo} e ${divisor} é: ${inteiro}')
    print(f'O resto da divisão entre ${dividendo} e ${divisor} é: ${resto}')
