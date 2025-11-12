renda = float(input())

if renda >= 0 and renda <= 2000:
    imposto_faixa_1 = 0
    print('Isento')
elif renda >= 2000.01 and renda <= 3000:
    renda_taxada = renda - 2000
    imposto_total_faixa_2 = (renda_taxada * 8) / 100
    print('R$ {:.2f}'.format(imposto_total_faixa_2))
elif renda >= 3000.01 and renda <= 4500:
    imposto_faixa_2 = (1000 * 8) / 100 
    imposto_faixa_3 = ((renda - 3000) * 18) / 100
    imposto_total_faixa_3 = imposto_faixa_2 + imposto_faixa_3
    print('R$ {:.2f}'.format(imposto_total_faixa_3))
elif renda > 4500:
    imposto_faixa_2 = (1000 * 8) / 100
    imposto_faixa_3 = (1500 * 18) / 100
    imposto_faixa_4 = ((renda - 4500) * 28) / 100
    imposto_total_faixa_4 = imposto_faixa_2 + imposto_faixa_3 + imposto_faixa_4
    print('R$ {:.2f}'.format(imposto_total_faixa_4))