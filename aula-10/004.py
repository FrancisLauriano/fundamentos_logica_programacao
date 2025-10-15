n_pares = 0
soma_pares = 0

while n_pares < 5:
    n = int(input('Digite: '))

    if n % 2 == 0:
        n_pares += 1
        soma_pares += n
        # print(n)


media_pares = soma_pares / n_pares
# print(f'QTD: {n_pares}')
print(f'Media: {media_pares}')


