menor = 0
maior = 0

for i in range(0, 5):
    peso = float(input(f'Informe o peso da {i+1}º pessoa: '))

    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Menor peso é: {menor}. Maior peso é: {maior}')                    
   