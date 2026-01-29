<<<<<<< HEAD
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
=======
num = float(input('Informe um número: '))

soma = num
media = num
maior = num
menor = num
qtd = 1

while True:

    continua = int(input('''Continuar digitando números?
[1] SIM
[2] NÃO
Opção: '''))
    
    
    if continua == 1:
        num = float(input('Informe um número: '))
        qtd += 1
        soma += num
        media = soma / qtd

        if num >= maior:
            maior = num
        if num <= menor:
            menor = num
        continue
    elif continua == 2:
        break
    else:
        print('Opção Inválida. Tente novamente!\n')
        continue

print(f'''Média: {media}
Maior: {maior}
Menor: {menor}''')

    

    
    

>>>>>>> 45e4ac0c4c238c0634ecaecd8c4d2657ede0bef5
