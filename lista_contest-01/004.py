teste = int(input('Testes: '))

for _ in range(teste):
    num1, num2 = map(str, input('Número: ').split())

    inicio_comparacao = len(num1) - len(num2)

    encaixa = True

    for i in range(len(num2)):
        if num1[inicio_comparacao + i] != num2[i]:
            encaixa = False
            break
    
    if encaixa:
        print('encaixa')
    else:
        print('não encaixa')

