
primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))
termo = 1
resultado = ''

while True:

    while termo <= 10:
        resultado += f'{primeiro}, ' + ''
        primeiro += razao
        termo += 1

    print(resultado.rstrip(', '))
