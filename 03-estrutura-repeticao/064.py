soma = 0
qtd = 0

while True:
    num = float(input('Informe um número: '))

    if num == 999:
        break

    soma += num
    qtd += 1

print(f'''Qtd números digitados: {qtd}
Soma: {soma}''')
