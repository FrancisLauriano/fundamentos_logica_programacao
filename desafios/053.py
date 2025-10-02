frase = input('Digite a frase: ').strip().lower()

frase_sem_espaco = ''

for letra in frase:
    if letra != ' ':
        frase_sem_espaco += letra
print(f'Frase sem Espaço: {frase_sem_espaco}')

frase_invertida = ''

for i in range(len(frase_sem_espaco) - 1, -1, -1):
    frase_invertida += frase_sem_espaco[i]
print(f'Frase Invertida: {frase_invertida}')

if frase_sem_espaco == frase_invertida:
    print('É um Palíndromo')
else:
    print('Não um Palíndromo')    