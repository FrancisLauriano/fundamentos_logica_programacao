nome = input('Digite nome: ')

maiusculo = nome.upper()
print(f'Maiuculo: {maiusculo}')

minusculo = nome.lower()
print(f'Minusculo: {minusculo}')

remove_espaco = nome.replace(' ', '')
print(f'Sem espaço: {remove_espaco}')

qtd_letras = len(remove_espaco)
print(f'Quantidade de letras sem espaço: {qtd_letras}')

separa_nome = nome.split()
print(f'Nomes seperados em lista: {separa_nome}')

qtd_letra_primeiro_nome = len(separa_nome[0])
print(f'Quantidade letras primeiro nome: {qtd_letra_primeiro_nome}')
