soma_idade = 0
qtd_menos_vinte = 0
mais_velho = 0
nome_mais_velho = ''

for c in range(1, 5):
    nome = input(f'\nInforme o nome da {c}º pessoa: ')
    idade = int(input(f'Informe o idade da {c}º pessoa: '))
    sexo = input(f'Informe o sexo da {c}º pessoa \n[F] FEMININO\n[M] MASCULINO\nOpção: ').lower().strip()

    soma_idade += idade

    if sexo == 'm':
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome


    if sexo == 'f' and idade < 20:
        qtd_menos_vinte += 1


media_idade = soma_idade / 5

print(f'''\nMédia idade do grupo: {media_idade}
Homem mais velho é: {nome_mais_velho}
Quantidade de Mulheres com menos de 20 anos: {qtd_menos_vinte}''')