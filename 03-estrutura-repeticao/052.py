numero = int(input('Informe um número inteiro: '))

qtd_divisores = 0

for c in range(1, numero+1):
    if numero % c == 0:
        qtd_divisores += 1

if qtd_divisores == 2:
    print(f'{numero} é um número primo')
else:
    print(f'{numero} não é um número primo')
