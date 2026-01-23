soma = 0
qtd_num = 0

while qtd_num < 6:
    n = int(input(f'{qtd_num + 1}º número: '))
    qtd_num += 1

    if n % 2 == 0:
        soma += n
print(f'Soma: {soma}')
