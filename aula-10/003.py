# numero positivo: soma numeros positivos
# numero negativo: media dos numeros positivos

numero = 1
soma_positivo = 0
qtd_positivo = 0
media_positivo = 0

while numero > 0:
    numero = int(input('Informe um número inteiro: '))

    if numero < 0:
        print('Sistema finalizado')
        break

    qtd_positivo += 1
    soma_positivo += numero
    media_positivo = soma_positivo / qtd_positivo
    print(f'Soma positivos: {soma_positivo}')
    print(f'Média positivos: {media_positivo}')
print(f'Média positivos: {media_positivo}')

    






