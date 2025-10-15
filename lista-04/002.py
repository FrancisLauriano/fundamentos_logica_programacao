# -*- coding: utf-8 -*-

n = int(input('Quantos termos: '))

for i in range(0, n):

    n_binario = input('Digite o valor: ')

    decimal = 0
    expoente = 0

    # for digito in n_binario[::-1]:
        # decimal += int(digito) * (2**expoente)
        # expoente += 1
    for digito in n_binario:
        decimal = (decimal * 2 + int(digito)) % 1500
    
    print(f'Decimal: {decimal}')
        
    termo = decimal
    i = 2
    f1 = 0
    f2 = 1
    
    if termo == 0:
        fibonacci = 0
    elif termo == 1:
        fibonacci = 1
    else:
        while i <= termo:
            # fibonacci = f1 + f2
            fibonacci = (f1 + f2) % 1000
            i += 1
    
            f0 = f1
            f1 = f2
            # f2 = f2 + f0
            f2 = (f2 + f0) % 1000
    
    print('Fibonacci: {:03d}'.format(fibonacci))