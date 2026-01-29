qtd_um = 0
qtd_dez = 0
qtd_vinte = 0
qtd_cinquenta = 0

while True:
    valor = int(input('\nValor a ser sacado R$: '))

    qtd_cinquenta = valor // 50
    resto_cinquenta = valor % 50

    qtd_vinte = resto_cinquenta // 20
    resto_vinte = resto_cinquenta % 20

    qtd_dez = resto_vinte // 10
    resto_dez = resto_vinte % 10

    qtd_um = resto_dez // 1
    

    print(f'''\n{'='*30}
Quantidade células R$50,00: {qtd_cinquenta}
Quantidade células R$20,00: {qtd_vinte}
Quantidade células R$10,00: {qtd_dez}
Quantidade células R$1,00: {qtd_um}
{'='*30}\n''')
    
    while True:
        continua = input('Deseja continuar sacando? [S] SIM [N] NÃO: ').lower()

        if continua != 's' and continua != 'n':
            print(f'Opção Inválida! Tente novamente...\n')
            continue
        else:
            break
    
    if continua == 's':
        continue
    else:
        break

print(f'\nOperação finalizada!')



