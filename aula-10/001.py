# positivo, negativo, zero finaliza o programa
numero = 1
i = 0

while numero != 0:
    numero = int(input('Digite um número inteiro: '))

    if numero > 0:
        print('Positivo')
    elif numero < 0:
        print('Negativo')  
    i += 1 

    if numero == 0:
        print(f'Repetição: {i-1}') # -1 para não contar com 0 digitado (não contar com flag)
        break

# OU

numero = 1
i = 0

while numero != 0:
    numero = int(input('Digite um número inteiro: '))

    if numero > 0:
        print('Positivo')
        i += 1 
    elif numero < 0:
        print('Negativo')  
        i += 1 

    if numero == 0:
        print(f'Repetição: {i}')
        break


