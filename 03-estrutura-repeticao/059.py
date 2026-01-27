n1 = float(input(f'Primeiro número: '))
n2 = float(input(f'Segund0 número: '))

while True:

    opcao = int(input('''Escolha uma opção a seguir:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair

Opção: '''))
    
    if opcao == 1:
        soma = n1 + n2
        print(f'\nResultado Soma: {soma}\n') 
        continue      
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'\nResultado Multiplicação: {multiplicacao}\n')
        continue
    elif opcao == 3:
        maior = 0
        if n1 >= maior:
            maior = n1
        if n2 >= maior:
            maior = n2
        print(f'\nResultado Maior: {maior}\n') 
        continue 
    elif opcao == 4:
        n1 = float(input(f'Primeiro número: '))
        n2 = float(input(f'Segund0 número: '))
        continue
    elif opcao == 5:
        print(f'Saindo... ')
        break
    else:
        print(f'Opção inválida.\nTente novamente!\n')
        continue

    