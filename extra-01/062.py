primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
total_termos = 10

while True:
    i = 1
    while i <= total_termos:
        print(termo)
        termo += razao
        i += 1

    total_termos = int(input('Mais termos: Quantos? '))

    if total_termos == 0:
        break


# OU
    
while total_termos != 0:
    i = 1
    while i <= total_termos:
        print(termo)
        termo += razao
        i += 1

    total_termos = int(input('Mais termos: Quantos? '))
