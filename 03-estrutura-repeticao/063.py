num = int(input('Informe o valor: '))

fibonacci = 1

if num == 1 or num == 2: 
    print(f'F{num}: {fibonacci}')
else:

    termo = 2
    fn1 = 1
    fn2 = 1

    while num > termo:
        fibonacci = fn1 + fn2
        fn2 = fn1
        fn1 = fibonacci
        termo += 1
    print(f'F{num}: {fibonacci}')