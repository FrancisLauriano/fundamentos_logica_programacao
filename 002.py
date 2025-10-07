
n1, n2 = map(int, input('Digite dois números: ').split())

if n1 > n2:
    maior = n1
    menor = n2

else:
    maoir = n2
    menor = n1

i = menor 

while i < maior:
    if (menor % 2 == 0) and (menor % 6 != 0):
            print(i)
            i += 1
 
