usuario1 = 'francis'
usuario2 = 'silva'
senha_valida = '1234'

login = input('Informe o usuário: ')

if login == usuario1 or login == usuario2:
    senha = input('Informe a senha:')    

    if senha == senha_valida:
        print('Login realizado com sucesso.')
    else:
        print('Senha inválida.')    
else:
    print('Usuário inválido..\nAplicação finalizada.')