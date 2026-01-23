numero_string = '47'

trata_digito = '{:>04}'.format(numero_string)
print(f'Número string: {trata_digito}')
print(f'Unidade: {trata_digito[3]}')
print(f'Dezena: {trata_digito[2]}')
print(f'Centena: {trata_digito[1]}')
print(f'Milhar: {trata_digito[0]}')

###############################################

numero = 47

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')