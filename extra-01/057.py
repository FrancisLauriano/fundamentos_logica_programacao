sexo = ''

while sexo != 'F' and sexo != 'M':
    sexo = input('Informe o sexo [M] Masculino [S] Feminino: ').upper()

print('FIM')

# OU

while True:
    sexo = input('Informe o sexo [M] Masculino [S] Feminino: ').upper()

    if sexo == 'F' or sexo == 'M':
        break
print('FIM')