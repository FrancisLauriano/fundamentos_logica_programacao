N1, N2, N3, N4, N5, N6 = map(float, input('Infome seis números: ').split())

quantidade = 0
soma = 0

if N1 > 0:
    quantidade += 1
    soma += N1
if N2 > 0:
    quantidade += 1
    soma += N2
if N3 > 0:    
    quantidade += 1
    soma += N3
if N4 > 0:
    quantidade += 1
    soma += N4
if N5 > 0:
    quantidade += 1
    soma += N5
if N6 > 0:
    quantidade += 1
    soma += N6

media = soma / quantidade

print(f'{quantidade} valores positivos')
print('{:.1f}'.format(media))


# quantidade = 0
# soma = 0

# for i in range(6):
#     num = float(input(f'Informe o {i+1}º número: '))
#     if num > 0:
#         quantidade += 1
#         soma += num

# media = soma / quantidade

# print(f'{quantidade} valores positivos')
# print('{:.1f}'.format(media))