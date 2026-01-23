frase = input('Frase: ').lower()

frase_invertida = ''
frase_sem_espaco = ''

for letra in frase:
    if letra not in ' ':
        frase_sem_espaco += letra

frase_invertida = frase_sem_espaco[::-1]

if frase_sem_espaco == frase_invertida:
    print('É Palíndomo')
else:
    print('Não é Palíndomo')

print(frase_invertida)