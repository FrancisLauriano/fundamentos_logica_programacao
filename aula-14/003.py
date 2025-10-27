n1, n2 = map(int, input('Dois números inteiros: ').split())

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for c in range(menor, maior + 1):
    soma = 0
    for d in range(1, c):
        if c % d == 0:
            soma += d
    
    if soma == c:
        print(c)
