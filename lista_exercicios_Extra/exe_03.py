num1, num2 = map(float, input('Informe dois números: ').split())

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num2} é maior que {num1}')    
else:
    print('Os números são iguais')    