divisor = 0
soma = 0

numero = int(input('Informe um número: '))


for c in range(1, numero):

    if numero % c == 0:
        soma += c

if numero == soma:
    print(f'A soma dos seus divisores é: {soma}\n"{numero}" é um número perfeito')
else:
    print(f'A soma dos seus divisores é: {soma}\n"{numero}" NÃO é um número perfeito')