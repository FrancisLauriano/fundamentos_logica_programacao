n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

opcao = None

while opcao != 5:
    opcao = int(input('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Informe a opção: '''))
    if opcao == 1:
        soma = n1 + n2
        print(f'\nResultado Soma: {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'\nResultado Multiplicação: {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print(f'\n{n1} é maior que {n2}')
        elif n2 > n1:
            maior = n2
            menor = n1
            print(f'\n{n2} é maior que {n1}')
        else:
            print(f'\n{n1} é igual a {n2}')
    elif opcao == 4:
        n1 = float(input('\nDigite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('\nSair ...')
        exit()
    else:
        print('\nOpção Inválida!')    






