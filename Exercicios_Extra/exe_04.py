qtd_compra = int(input('Informe a quantidade de produtos comprados: '))

if qtd_compra < 0:
    print('Quantidade inválida')
else:    
    if qtd_compra > 15:
        valor_unit = 0.25       
    else:
        valor_unit = 0.30
    valor_final = qtd_compra * valor_unit
    print('Valor da compra R$ {:.2f}'.format(valor_final))    