primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Razão da PA: '))

ultimo = primeiro + (razao * 10)

for i in range(primeiro, ultimo, razao):
    print(i)
