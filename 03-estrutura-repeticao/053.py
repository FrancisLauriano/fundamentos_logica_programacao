frase = input('Informe a frase: ').lower().strip()

frase_sem_espaco = frase.replace(' ', '')

frase_invertida = ''

for c in range(len(frase_sem_espaco)-1, -1, -1):
    frase_invertida += frase_sem_espaco[c]

if frase_invertida == frase_sem_espaco:
    print(f'É Palíndromo!')
else:
    print(f'Não é Palíndromo!')


# print(frase_invertida)
