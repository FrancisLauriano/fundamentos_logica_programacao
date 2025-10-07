# n = int(input('Informe um número: '))
# numero = n
# numero = int(input('Informe um número: '))

# i = 1
# fatorial = 1
# n = numero

# if n == 0 or n == 1:
#     print(f'{numero}! = {fatorial}')
# else:
#     while n >= i:
#         fatorial *= n
#         n -= 1   
#     print(f'{numero}! = {fatorial}')


        
numero = int(input('Informe um número: '))

n = numero
fatorial = 1

if n == 0 or n == 1:
    print(f'{numero}! = {fatorial}')
else:
    while n >= 1:
        fatorial *= n
        n -= 1 
    print(f'{numero}! = {fatorial}')    
