# -*- coding: utf-8 -*-

n = int(input(''))

for i in range(0, n):

    n_binario = input('')

    decimal = 0
    expoente = 0

    # for digito in n_binario[::-1]:
        # decimal += int(digito) * (2**expoente)
        # expoente += 1
    for digito in n_binario:
        decimal = (decimal * 2 + int(digito)) % 1500
        
    
    fibonacci = 1
    termo = decimal
    i = 3
    f1 = 1
    f2 = 1
    
    if termo == 0:
        fibonacci = 0
    elif termo == 1 or termo == 2:
        fibonacci = fibonacci
    else:
        while i <= termo:
            # fibonacci = f1 + f2
            fibonacci = (f1 + f2) % 1000
            i += 1
    
            f0 = f1
            f1 = f2
            # f2 = f2 + f0
            f2 = (f2 + f0) % 1000
    
    print('{:03d}'.format(fibonacci))