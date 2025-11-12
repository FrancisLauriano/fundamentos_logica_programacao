num1, num2, num3 = map(float, input('Informe três números: ').split())

soma = num1 + num2 + num3

if soma > 10:
    print(f'Limite Excedido. Soma: {soma}\nAplicação Finalizada.')
else:
    print('Operação realizada com sucesso.')    