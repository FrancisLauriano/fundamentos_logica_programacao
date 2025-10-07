sexo = input('Informe sexo [M] [F]: ').lower()

while sexo != 'm' and sexo != 'f':
    print('Opção Inválida!')
    sexo = input('Informe sexo [M] [F]: ').lower()

print('Opção Válida!')
