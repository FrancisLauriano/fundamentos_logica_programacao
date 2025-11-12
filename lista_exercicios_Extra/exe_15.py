# AULA 8 - Estruturas Condicionais - 12/09/2025
# 6. Faça uma aplicação que solicite o nome e a data de nascimento de dois usuários e indique qual deles é o mais velho.

usuario1 = input('Infome nome 1º usuário: ')
dia1, mes1, ano1 = map(int, input('Informe a data de nascimento do 1º usuário(DD/MM/AAAA): ').split('/'))
usuario2 = input('Infome nome 2º usuário: ')
dia2, mes2, ano2 = map(int, input('Informe a data de nascimento do 2º usuário(DD/MM/AAAA): ').split('/'))

if (ano1 > 0 and ano2 > 0) and (mes1 > 0 and mes1 <= 12) and (mes2 > 0 and mes2 <= 12) and (dia1 > 0 and dia1 <= 31) and (dia2 > 0 and dia2 <= 31):
    if ano1 < ano2:
        print(f'{usuario1} é mais velho que {usuario2}')
    elif ano1 == ano2:
        if mes1 < mes2: 
            print(f'{usuario1} é mais velho que {usuario2}') 
        elif mes1 == mes2:
            if dia1 < dia2:
                print(f'{usuario1} é mais velho que {usuario2}') 
            elif dia1 == dia2:
                print(f'{usuario1} e {usuario2} tem a mesma idade') 
            else:    
               print(f'{usuario2} é mais velho que {usuario1}') 
        else:  
            print(f'{usuario2} é mais velho que {usuario1}')
    else:
        print(f'{usuario2} é mais velho que {usuario1}')
else:
    print('Data de nascimento inválida')
