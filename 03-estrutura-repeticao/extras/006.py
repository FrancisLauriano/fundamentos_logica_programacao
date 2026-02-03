n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))


print(f'\nOs números perfeiros entre {n1} e {n2}: ')
for i in range(n1, n2+1):
    soma = 0

    for c in range(1, i):
        if i % c == 0:
            soma += c

    if soma == i:
        print(f'{i}, ', end='')