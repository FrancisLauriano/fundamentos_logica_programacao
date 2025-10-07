N = int(input('Informe o valor: '))

i = 0
media = 0

while i < N:
    nota1, nota2, nota3 = map(float, input('Informe as três notas: ').split())
    
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
    print('{:.1f}'.format(media))

    i +=1