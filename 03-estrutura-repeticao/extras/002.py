qtd_pares = 0
soma = 0

while qtd_pares < 5:
    numero = int(input('Informe um número: '))

    if numero % 2 == 0:
        qtd_pares += 1
        soma += numero

media = soma / qtd_pares

print(f'Média dos {qtd_pares} pares: {media:.2f}')

