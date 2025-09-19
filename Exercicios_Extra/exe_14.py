# AULA 8 - Estruturas Condicionais - 12/09/2025
# 5. Faça um programa que tenha alvo 3 usuários e 3 senhas para cada um dos usuários (isso não é um input), 
# então a aplicação irá solicitar um usuário, caso ele seja inválido avise e finalize a aplicação, 
# caso ele seja verdadeiro então solicite a senha, caso ele acerte a senha informe que o login foi realizado com sucesso, 
# caso não avise que a senha é inválida e finalize a aplicação.

# opção 1:
usuario1 = 'francis'
senha1 = '1234'
usuario2 = 'joao'
senha2 = '4567'
usuario3 = 'silva'
senha3 = '7890'

usuario = input('Informe o usuário: ')

if usuario == usuario1 or usuario == usuario2 or usuario == usuario3:
    senha = input('Informe a senha: ')
    if (usuario == usuario1 and senha == senha1) or (usuario == usuario2 and senha == senha2) or (usuario == usuario3 and senha == senha3):
        print('Login realizado com sucesso')
    else:
        print('Senha Inválida')
else:
    print('Usuário inválido')        


# opção 2:
usuarios = {
    'francis': '1234',
    'joao': '4567',
    'silva': '7890'
} 

usuario = input('Informe o usuário: ')

if usuario in usuarios:
    senha = input('Informe a senha:')
    if senha == usuarios[usuario]:
        print('Login realizado com sucesso')
    else:
        print('Senha inválida')
else:
    print('Usuário inválido')            


    