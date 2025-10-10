soma = 0
i = 0

while True:
    n = int(input('Informe um número: '))

    if n == 999:
        break

    soma += n
    i += 1
print(f'\nNúmeros digitados: {i}')
print(f'Soma: {soma}')