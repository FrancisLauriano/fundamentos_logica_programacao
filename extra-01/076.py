def meus_fornecedores(fornecedores_precos: tuple) -> str:
    tabulacao = ''

    for indice, item in enumerate(fornecedores_precos):
        if indice % 2 == 0:
            fornecedor = item
        else:
            preco = item
            tabulacao += f'| Fornecedor: {fornecedor} | Preço R$: {preco:.2f}|\n'
    return tabulacao

tupla_fornecedores_precos = 'Fornecedor B', 12.10, 'Fornecedor A', 20.70, 'Fornecedor C', 15.50
print(meus_fornecedores(tupla_fornecedores_precos))