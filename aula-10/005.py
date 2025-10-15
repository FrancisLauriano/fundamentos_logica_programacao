while True:

    mes = int(input('Infome o mês: '))

    if mes > 12 or mes < 1:
        print('Mês Inválido! Informe valor válido')
        continue

    while True:

        dia = int(input('Infome o dia: '))

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 31 or dia < 1:
                print('Dia Inválido! Informe valor válido')
                continue
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30 or dia < 1:
                print('Dia Inválido! Informe valor válido')
                continue
        
        break

    break