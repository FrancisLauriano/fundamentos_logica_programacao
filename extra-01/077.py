def encontrar_vogais(palavras: tuple) -> str:
    resultado = ''
    resultados = ''

    for palavra in palavras:
        vogais = ''
        for item in palavra:
            if item in 'AEIOUaeiou':
                vogais += item
                resultado = f'Palavra: {palavra} | Vogais: {vogais}\n'
        resultados += resultado

    return resultados
                


palavras = 'Francis', 'Lauriano', 'Silva'
print(encontrar_vogais(palavras))