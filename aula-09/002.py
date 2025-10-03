SENHA = '1234'

senha_usuario = input('Digite sua senha: ')

while senha_usuario != SENHA:
    print('ACESSO NEGADO!')
    senha_usuario = input('\nInforme sua senha: ')
print('ACESSO LIBERADO!')    