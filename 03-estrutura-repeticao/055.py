maior = 0
menor = 10000

for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}º pessoa: '))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    
print(f'Maior peso é: {maior} kg.\nMenor peso é {menor} kg')

