n = int(input('Informe um número: '))

soma = 0

for i in range(1, n):
    if n % i == 0:
        print(i)
        soma += i
    
if soma == n:
    print(f'{n} é um número perfeito')
else:
    print(f'{n} NÃO é um número perfeito')

# OU
    
soma = 0
i = 1

while i < n:
    if n % i == 0:
        print(i)
        soma += i
    i += 1

if soma == n:
    print(f'{n} é um número perfeito')
else:
    print(f'{n} NÃO é um número perfeito')

