hora, min = map(int, input('Informe a hora no formato HH:MM').split(':'))
if (hora < 0 or hora > 23) or (min < 0 or min > 59):
    print('Hora inválida')
elif hora >= 0 and hora < 6:
    print('É Madrugada') 
elif hora >= 6 and hora < 12:   
    print('Bom dia')   
elif hora >= 12 and hora < 18:
    print('Boa tarde')
else:
    print('Boa noite')  
