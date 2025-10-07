primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

i = primeiro_termo

while ((razao*10) + primeiro_termo) > i:
    print(i)
    i += razao