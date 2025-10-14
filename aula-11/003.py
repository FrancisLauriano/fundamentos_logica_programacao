n1, n2 = map(int, input('Digite dois número: ').split())

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

soma = 0

for i in range(menor, maior+1):
    soma += i

print(soma)