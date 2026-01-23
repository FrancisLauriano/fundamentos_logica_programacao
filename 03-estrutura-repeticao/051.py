primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))



ultimo_termo = primeiro_termo + (razao * 10)
n = 1

for c in range(primeiro_termo, ultimo_termo, razao):
    print(f'{n}º termo: {c}')
    n+=1


######################

n_termo = 1
termo = primeiro_termo

while n_termo <= 10:
    print(f'{n_termo}º termo: {termo}')
    termo += razao
    n_termo += 1