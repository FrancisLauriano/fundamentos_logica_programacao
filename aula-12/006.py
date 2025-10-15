palavra = input('Informe uma palavra: ')

invertido = ''
for letra in palavra[::-1]:
    invertido += letra

print(invertido)

# OU

invertido = ''
i = len(palavra)-1
while i >= 0:
    invertido += palavra[i]
    i -= 1

print(invertido)