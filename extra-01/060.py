n = int(input('Informe o valor inteiro: '))

i = n
fatorial = 1

if n == 0 or n == 1:
    print(f'{n}! = {fatorial}')
else:
    while i >= 1:
        print(i)
        fatorial *= i
        i -= 1 
    print(f'{n}! = {fatorial}')
