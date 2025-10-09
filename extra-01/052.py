n = int(input('Informe número inteiro: '))

divisor = 0

for i in range(n, 0, -1):
    if n % i == 0:
        divisor += 1
        
if divisor > 2:
    print('Não é primo!')
else: 
    print('É PRIMO')