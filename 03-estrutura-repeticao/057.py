# sexo = ' '

# while sexo not in 'MmFf':
#     sexo = input('Digite F para Feminino e M para masculino: ')

#####################

while True:
    sexo = input('Digite F para Feminino e M para masculino: ')

    if sexo in 'FfMm':
        break
    else:
        print(f'Valor inválido! Tente novamente!\n')
        continue