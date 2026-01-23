primeiro_termo = int(input('Termo: '))
pa = int(input('PA: '))

ultimo_termo = primeiro_termo + (pa * 10)

for i in range(primeiro_termo, ultimo_termo, pa):
    print(i)
