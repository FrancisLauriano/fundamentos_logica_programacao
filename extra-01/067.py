while True:
    print('-'*50)
    n = int(input('Quer ver a tabuada de qual número: '))
    print('-'*50)

    if n < 0:
        break

    i = 0

    while i <= 10:
        print(f'{i} x {n} = {i*n}')
        i += 1

print('\nPrograma finalizado!')