qtd_divisor = 0


n = int(input('Informe um número inteiro: '))

for c in range(n, 0, -1):
    if n % c == 0:
        qtd_divisor += 1

if qtd_divisor > 2:
    print(f'O número {n} NÃO é Primo!')
else:
    print(f'O número {n} é Primo!')    