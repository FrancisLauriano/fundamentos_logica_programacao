n_linha = int(input('Qtd linhas? ').strip())

for i in range(n_linha):

    linha = input(f'Digite linha {i+1}: ').strip()

    codigo_passo_um = ''
    codigo_passo_dois = ''
    codigo_passo_tres = ''

    for c in linha:
        if c.isalpha():
            posicao = ord(c) + 3
        else:
            posicao = ord(c)
        # novo_caractere  = chr(posicao)
        # codigo_passo_um += novo_caractere
        codigo_passo_um += chr(posicao)


        # print(codigo_passo_um)

    # for d in range(len(codigo_passo_um) - 1, -1, -1):
    #     codigo_passo_dois += codigo_passo_um[d]
        # print(codigo_passo_dois)

    codigo_passo_dois = codigo_passo_um[::-1]
    
    # print(codigo_passo_dois)

    metade_caractere = len(codigo_passo_dois) // 2

    for indice, e in enumerate(codigo_passo_dois):
        if indice >= metade_caractere:
            posisao = ord(e) - 1
        else:
            posisao = ord(e)

        # novo_caractere = chr(posisao)
        # codigo_passo_tres += novo_caractere
        codigo_passo_tres += chr(posisao)


    print(codigo_passo_tres)