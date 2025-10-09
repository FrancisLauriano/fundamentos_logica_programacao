soma = 0

while True:
    n = int(input('Informe um número: '))

    if n == 999:
        break

    soma += n
print(f'\nSoma: {soma}')