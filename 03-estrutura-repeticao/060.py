n = int(input('Informe um número: '))
fatorial = 1
calculo = ''

for c in range(n, 0, -1):
    calculo += f'{c}x' + ''
    fatorial *= c

print(f'{n}!={calculo.rstrip('x')}={fatorial}')
