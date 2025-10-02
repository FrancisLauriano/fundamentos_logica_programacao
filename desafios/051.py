primeiro_termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

for c in range(primeiro_termo, primeiro_termo + (10 * razao), razao):
    print(f'{c}')
print('FIM')    