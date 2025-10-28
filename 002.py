def maior_valor(*numero):
    maior = 0

    for i in numero:
        if i > maior:
            i = maior
    return maior

def manor_valor(*numero):
    menor = 1000000000000000

    for i in numero:
        if i < menor:
            i = menor
    return menor
 

def media_valores(*numero):
    soma = 0
    qtd_numero = 0

    for i in numero:
        soma += i
        qtd_numero += 1
    media = soma / qtd_numero
    return media


valores = map(map, input('Digite os valores: ').split())
# media = media_valores(10, 20, 30, 40, 60)
media = media_valores(*valores)
print(media)
