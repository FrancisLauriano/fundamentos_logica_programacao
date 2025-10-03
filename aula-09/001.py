
# # numero
# n = int(input('Digite número inteiro: '))

# # iteirador
# i  = 0

# # enquanto meu iteirador for menor ou igual ao numero, ele repete e iteira um valor X a minha variavel de iteração i
# while i <= n:
#     # printar començando de zero
#     print(i)

#     # iteirar 1 ao contador enquanto a condição verdadeira
#     i += 1
    
# print('FIM')


# n = int(input('Digite número inteiro: '))

# i = 0

# while i < n:
#     print(i * 2)
#     i += 1

# print('FIM')    

SENHA = '1234'

senha_usario = input('Informe a senha: ')

while senha_usario != SENHA:
    print('ACESSO NEGADO!')
    senha_usario = input('Informe a senha: ')
    
print('ACESSO PRMITIDO!')    
    