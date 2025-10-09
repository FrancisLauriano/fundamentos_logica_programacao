media_idade = 0
soma_idade = 0
nome_mais_velho = ''
idade_mais_velho = 0
mulheres_menos_vinte = 0
total_pessoas = 0

for i in range(1, 5):
    nome = input(f'\nNome da {i}º pessoa: ')
    idade = int(input(f'Idade da {i}º pessoa: '))
    sexo = input(f'Sexo da {i}º pessoa [F] Feminino [M] Masculino: ').lower()

    soma_idade += idade
    total_pessoas += 1

    if (sexo == 'f') and (idade < 20):
        mulheres_menos_vinte += 1
    
    if (sexo == 'm'):
        if i == 1:
           idade_mais_velho = idade
           nome_mais_velho = nome
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

media_idade = soma_idade / total_pessoas

print(f'\nMedia idade grupo: {media_idade}')
print(f'Nome do mais velho: {nome_mais_velho}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres_menos_vinte}')
