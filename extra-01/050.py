soma = 0

for i in range(0, 6):
    n = int(input(f'Informe o {i+1}º número: '))

    if n % 2 == 0:
        soma += n
print(f'Soma: {soma}')