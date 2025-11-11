def filtro_int(vetor: list, num: int) -> list:
    qtd = vetor.count(num)

    i = 0

    while i < qtd:
        vetor.remove(num)
        i += 1
    return vetor


print(filtro_int([1, 2, 3, 4, 5, 5, 5], 5))

# def filtro_recusivo(vetor, numero):
#     if vetor == []:
#         return vetor
#     elif 

