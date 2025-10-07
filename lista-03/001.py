# contém um valor inteiro N (N < 10000)
N = int(input('Quantidade de números'))

i = 0
intervalo = 0
no_intervalo = 0


while (i < N) and (i < 10000):
    numero = int(input(f'{i+1} número'))
    i += 1
    
    if (numero >= 10) and (numero <= 20):
        intervalo += 1
    else:
        no_intervalo += 1

print(f'{intervalo} in')
print(f'{no_intervalo} out')
