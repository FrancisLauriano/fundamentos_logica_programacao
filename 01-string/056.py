soma = 0
qtd_mulheres_mais_vinte = 0
idade_mais_velho = 0
nome_mais_velho = ''

for c in range(1, 5):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    soma += idade

    if sexo in 'Mm':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome
    else:
        if idade < 20:
            qtd_mulheres_mais_vinte += 1

media = soma / 5
print(f'Media: {media}')
print(f'Homem mais velho: {nome_mais_velho}')
print(f'Quantidade de mulheres menores 20 anos: {qtd_mulheres_mais_vinte}')
