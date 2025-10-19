n = int(input())

for i in range(0, n):
    qtd_1, qtd_2 = map(int, input().split())
    
    if qtd_1 > qtd_2:
        maior = qtd_1
        menor = qtd_2
    else: 
        maior = qtd_2
        menor = qtd_1

    # for c in range(1, maior + 1):
    #     if maior % c == 0 and menor % c == 0:
    #         mmc = c

    # print(mmc)

    # mmc por euclides
    while menor != 0:
        resto_divisao = maior % menor
        maior = menor
        menor = resto_divisao
    print(maior)






