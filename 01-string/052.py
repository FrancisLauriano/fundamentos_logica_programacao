num = int(input('Numero: '))

qtd_divisores  = 0

for c in range(1, num + 1):
    if num % c == 0:
        qtd_divisores += 1

if qtd_divisores == 2:
    print('É primo')
else:
    print('Não é primo')