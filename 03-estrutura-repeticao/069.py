qtd_mais_dezoito = 0
qtd_homem = 0
qtd_mulher_menos_vinte = 0


while True:
    idade = int(input('Informe a idade: '))
    

    while True:
        sexo = input('Informe o sexo -> [F] Feminino [M] Masculino: ')

        if sexo != 'f' and sexo != 'm':
            print(f'Valor inválido. tente novamente\n')
            continue
        else:
            break

    while True:
        continua = input('Deseja continuar? [S] SIM [N] NÃO: ').lower()

        if continua != 's' and continua != 'n':
            print(f'Valor Inválido. Tente novamente!\n')
            continue
        else:
            break

    if idade > 10:
        qtd_mais_dezoito += 1
    if sexo == 'm':
        qtd_homem += 1
    if sexo == 'f' and idade < 20:
        qtd_mulher_menos_vinte += 1


    if continua == 's':
        continue
    else:
        break

print(f'Pessoas com mais 18 anos: {qtd_mais_dezoito}\nHomens Cadastrados: {qtd_homem}\nMulheres menos de 20 anos: {qtd_mulher_menos_vinte}')

    