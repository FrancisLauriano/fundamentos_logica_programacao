maior = 0
menor = 10000

for c in range(1, 7):
    peso = float(input('Peso: '))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'Maior: {maior} Menor: {menor}')