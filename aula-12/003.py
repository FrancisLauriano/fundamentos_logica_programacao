n = int(input('Infome um número inteiro: '))

fatorial = 1

if n == 1 or n == 0:
    fatorial = fatorial
else:
    for i in range(1, n + 1):
        fatorial *= i
print(f'Fatorial de {n}! é {fatorial}')


# OU

fatorial = 1
i = 1

if n == 1 or n == 0:
    fatorial = fatorial
else:
    while i <= n:
        fatorial *= i
        i += 1
    
print(f'Fatorial de {n}! é {fatorial}')