# imprimir os pares e não multiplos de 6 entre o intervalo  de dois numeros

n1, n2 = map(int, input('Digite dois números inteiros: ').split())

if n1 >= n2:
    maior = n1
    menor = n2
else: 
    maior = n2
    menor = n1

i = menor

while i < maior:
    if i % 2 == 0:
        if i % 6 != 0:
            print(i) 
    i += 1


       


 
