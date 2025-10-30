def filtra_vogal(palavra: str) -> str:
    palavra_filtrada = ''
    for letra in palavra:
        if letra not in 'aeiouAEIOU':
            palavra_filtrada += letra
    
    return palavra_filtrada

palavra = input('Informe uma palavra: ')
resultado = filtra_vogal(palavra)
print(resultado)