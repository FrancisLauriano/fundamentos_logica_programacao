while True:
    num = int(input('Informe um número: '))

    if num < 0:
        break
    
    print(f'='*20)
    for c in range(0, 11):
        print(f'{num} x {c} = {num*c}')

    print(f'='*20,'\n')
