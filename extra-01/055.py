maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Informe o peso da {i}º pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso


print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')