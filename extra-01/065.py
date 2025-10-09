media = 0
soma = 0
qtd_n = 0
maior = 0
menor = 0

while True:
    n = int(input('\nDigite um número: '))

    soma += n
    qtd_n += 1

    if qtd_n == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    
    continuar = int(input('''\n[1] Sim [2] Não
    Continuar? '''))

    if continuar == 1:
        continue
    elif continuar == 2:
        break
    else:
        print('Opção inválida!')
        continue

media = soma / qtd_n
print(f'\nMaior: {maior} | Menor: {menor} | Média: {media:.1f}')


