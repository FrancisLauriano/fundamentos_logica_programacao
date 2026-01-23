soma = 0

for c in range(1, 7):
    numero = int(input(f'Informe o {c}º número: '))

    if numero % 2 == 0:
        soma += numero

print(f'Soma dos números pares: {soma}')