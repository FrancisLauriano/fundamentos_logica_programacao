frase = input('Digite uma frase: ').lower()

# remover espaço
frase_sem_espaco = ''

for letra in frase:
    if letra != ' ':
        frase_sem_espaco += letra
print(frase_sem_espaco)

frase_invertida = ''
# inverter a frase
for i in range((len(frase_sem_espaco) - 1), -1, -1):
    frase_invertida += frase_sem_espaco[i]

print(frase_invertida)

if frase_invertida == frase_sem_espaco:
    print('É Políndromo')
else:
    print('NÃO é Políndromo')