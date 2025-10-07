numero =1

while numero != 0:
    numero = int(input('Digite número: '))
    i = 0
    soma = 0
    qtd_positivos = 0
    media = 0
    
    if numero > 0:
        soma += numero
        qtd_positivos = 0
        print(f'Soma positivos: {soma}')
    elif numero < 0:
        media = soma / qtd_positivos
        print(f'Media positivos: {media}')
    else:
        break    



