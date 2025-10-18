n_linha = int(input())
todas_linhas = ''

for i in range(n_linha):

    linha = input()
    todas_linhas += linha + '\n'


    codigo_passo_um = ''
    codigo_passo_dois = ''
    codigo_passo_tres = ''

    for c in todas_linhas:
        if c.isalpha() == True:
            posicao = ord(c) + 3
        else:
            posicao = ord(c)
        novo_caractere  = chr(posicao)
        codigo_passo_um += novo_caractere

    for d in range(len(codigo_passo_um) - 1, -1, -1):
        codigo_passo_dois += codigo_passo_um[d]


    qtd_caractere = len(codigo_passo_dois)
    metade_caractere = qtd_caractere // 2

    for e in codigo_passo_dois:
        if codigo_passo_dois.find(e) >= metade_caractere:
            posisao = ord(c) - 1
        else:
            posisao = ord(c)

        novo_caractere = chr(posisao)
        codigo_passo_tres += novo_caractere

print(codigo_passo_tres)