# n1, n2 = map(int, input().split())

# if n1 >= n2:
#     maior = n1
#     menor = n2
# else:
#     maior = n2
#     menor = n1



# for i in range(menor, maior + 1):
#     soma_divisor = 0
#     for j in range(1, i):
#         if i % j == 0:
#             soma_divisor += j

#     if soma_divisor == i:
#         print(i)
#     # if menor % i == 0:
#     #     soma_divisor += i



n1, n2 = map(int, input().split())

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1



for i in range(menor, maior+1):
    soma = 0
    for j in range(1, i):
        if i % j == 0:
            soma += j

    if soma == i:
        print(i)






















