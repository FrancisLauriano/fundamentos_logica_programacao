total_valor = 0
qtd_prod_mais_mil = 0
produto_mais_barato = 100000000000000
nome_mais_barato = ''

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Valor R$: '))


    while True:
        continua = input('Deseja continuar? [S] SIM [N] NÃO: ').lower()

        if continua != 's' and continua != 'n':
            print(f'Opção Inválida. tente novamente!\n')
            continue
        else:
            break

    total_valor += preco
    if preco > 1000:
        qtd_prod_mais_mil += 1
    if preco <= produto_mais_barato:
        produto_mais_barato = preco
        nome_mais_barato = nome

    if continua == 's':
        continue
    else:
        break

print(f'Total gasto R$: {total_valor:.2f}\nQuantidade de produtos que custam mais de R$ 1.000,00: {qtd_prod_mais_mil}\nNome do produto mais barato: {nome_mais_barato}')
