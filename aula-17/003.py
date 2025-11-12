def uniao(lista_1: list, lista_2: list) -> list:
    lista_uniao = []
    lista_uniao = lista_1

    for i in lista_2:
        if i  not in lista_uniao:
            lista_uniao.append(i)

def intersessao(lista_1: list, lista_2: list) -> list:
    lista_intersecao = []
    
    for i in lista_1:
        if i in lista_2:
            lista_intersecao.append(i)
        
        lista_intersecao.sort()
        return lista_intersecao



