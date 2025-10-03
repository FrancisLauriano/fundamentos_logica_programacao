n1, n2 = map(int, input('Informe dois números: ').split())

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1  

while menor <= maior:
    print(menor)
    menor += 1
