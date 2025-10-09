primeiro = int(input('Digite primeiro termo da PA: '))
razao = int(input('Informe razão da PA: '))

termo = primeiro
i = 1

while i <= 10:
    print(termo)
    termo += razao
    i += 1