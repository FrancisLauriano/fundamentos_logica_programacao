soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma += c
print(f'Soma impares multiplos de 3 de 1 até 500: {soma}')