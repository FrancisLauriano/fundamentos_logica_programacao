# quantidade de cada letra

texto = input('Digitar texto: ').lower()

letra_verificada  = ''
resultados = ''

for letra in texto:
    if letra.isalpha() and letra not in letra_verificada:
        resultados += f'{{ {letra} :  {texto.count(letra)} }}'

        if letra != texto[-1]:
            resultados += ', '

        letra_verificada += letra
    
    
print(resultados)
        


