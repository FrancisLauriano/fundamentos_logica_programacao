soma_idades = 0
qtd_pessoa = 0
maior_idade_homem = 0
nome_maior_idade_homem = ''
qtd_mulheres_menos_20 = 0

for i in range(0, 4):
    nome = input(f'Informe o nome da {i+1}º pessoa: ').strip().lower()
    idade = int(input(f'Infome a idade da {i+1}º pessoa: '))
    sexo = input(f'Informe o sexo da {i+1}º pessoa: ').strip().lower()

    if (sexo == 'masculino') and (idade > maior_idade_homem):
        maior_idade_homem = idade
        nome_maior_idade_homem = nome


    if (sexo == 'feminino') and (idade < 20):
        qtd_mulheres_menos_20 += 1

    soma_idades += idade
    qtd_pessoa += 1

media_idade = soma_idades / qtd_pessoa    

print(f'Média idade do grupo é: {media_idade}')
print(f'Nome do homem mais velho: {nome_maior_idade_homem}')
print(f'Quantidade de mulheres que tem menos de 20 anos: {qtd_mulheres_menos_20}')