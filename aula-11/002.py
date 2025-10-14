n1, n2 = map(int, input('Dois valores inteiros: ').split())

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

# if menor % 2 == 0:
#     menor += 1

# for i in range(menor, maior+1, 2):
#     print(i)
for i in range(menor, maior+1):
    if i % 2 != 0:
        print(i)
