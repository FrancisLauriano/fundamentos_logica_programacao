palavra = input('Informe uma palavra: ')

qtd = 0

for letra in palavra:
    if letra in 'aA':
        qtd += 1

print(f'A palavra "{palavra}" tem {qtd} "aA"')

# OU 

qtd = 0
i = 0
while i <= len(palavra)-1:
    if palavra[i] in 'aA':
        qtd += 1
    i += 1

print(f'A palavra "{palavra}" tem {qtd} "aA"')