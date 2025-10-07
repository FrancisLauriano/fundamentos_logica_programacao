i = 0

while True:
    numero = int(input('Digite valor: '))

    if numero > 0:
        i += 1
        print('Positivo')
    elif numero < 0:
        i += 1
        print('Negativo')    
    else:
        print(i)
        break    

