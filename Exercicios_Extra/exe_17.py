N1, N2, N3, N4, N5 = map(int, input('Infome cinco números: ').split())

quantidade = 0

if N1 % 2 == 0:
    quantidade += 1
if N2 % 2 == 0:
    quantidade += 1
if N3 % 2 == 0:    
    quantidade += 1
if N4 % 2 == 0:
    quantidade += 1
if N5 % 2 == 0:
    quantidade += 1

print(f'{quantidade} valores pares')


# quantidade = 0

# for i in range(5):
#     num = int(input(f'Informe o {i+1}º número: '))
#     if num % 2 == 0:
#         quantidade += 1

# print(f'{quantidade} valores pares')