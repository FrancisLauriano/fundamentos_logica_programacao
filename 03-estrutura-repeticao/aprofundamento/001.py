ano_bissexto = False

mes, ano = map(int, input('Informe o mes e o ano: ').split())

if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    ano_bissexto = True

while True:
    dia = int(input('Informe o dia: '))

    if dia <= 0 or dia > 31:
        print(f'\nValor inválido. Tente novamente!\n')
        continue
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print(f'\nValor inválido. Tente novamente!\n')
            continue
        else:
            break
   
    elif mes == 2:
        if ano_bissexto == True and dia > 29:
            print(f'\nValor inválido. Tente novamente!\n') 
            continue
        elif ano_bissexto == False and dia > 28:
            print(f'\nValor inválido. Tente novamente!\n')
            continue
        else:
            break    
    else:
        break
    