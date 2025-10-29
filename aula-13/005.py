numero = int(input('Informe número inteiro: '))

qtd_divisores = 0

# testar ate a metade do numero (nenhum numero maior que numero/2 (considerar a divisão inteira) é divisor de numero, exceto ele mesmo)
for i in range(1, (numero // 2) + 1 ):
    if numero % i == 0:
        qtd_divisores += 1

qtd_divisores += 1  # somar 1 que é referente o próprio número (todo numero é divisivel por ele mesmo)

if qtd_divisores == 2:
    print(f'{numero} é PRIMO!')
else:
    print(f'{numero} NÃO É PRIMO')