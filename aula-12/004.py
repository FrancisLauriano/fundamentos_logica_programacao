n = int(input('Informe um número inteiro: '))

soma = 0

for i in range(0, n+1):
    if i % 2 != 0:
        soma += i
        print(i)

print(soma)

# OU

soma = 0
i = 0

while i <= n:
    if i % 2 != 0:
        soma += i
        print(i)
    i += 1

print(soma)