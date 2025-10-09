# soma = 0
# multiplicacao = 0
# maior = 0

n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))

while True:

    opcao = int(input('''\nQual opção deseja?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    Opção:  '''))

    if opcao == 1:
        soma = n1 + n2
        print(f'\nSoma: {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'\nMultiplicação: {multiplicacao}')
    elif opcao == 3:
        if n1 > n2: 
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        else:
            print(f'\n{n1} é igual a {n2}')
            exit()
        print(f'\n{maior} é maior que {menor}')
    elif opcao == 4:
        n1 = int(input('\nDigite primeiro número: '))
        n2 = int(input('Digite segundo número: '))
        continue
    elif opcao == 5:
        break
    else:
        print('Opção Inválida')
        continue

print('\nFim')