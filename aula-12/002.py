n1, n2 = map(int, input('Dois números inteiros: ').split())

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

qtd_numero = 0
soma = 0

for i in range(menor, maior + 1):
    print(i)
    soma += i
    qtd_numero += 1

media = soma / qtd_numero
print(f'Qtd: {qtd_numero}')
print(f'Soma: {soma}')
print(f'Media: {media}')

# OU

i = menor
qtd_numero = 0
soma = 0

while i <= maior:
    print(i)
    soma += i
    i += 1
    qtd_numero += 1
    

media = soma / qtd_numero
print(f'Qtd: {qtd_numero}')
print(f'Soma: {soma}')
print(f'Media: {media}')
