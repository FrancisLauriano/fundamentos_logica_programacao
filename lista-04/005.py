n = int(input())

for i in range(0, n):
    dieta = input()
    cafe = input()
    almoco = input()

    consumido = cafe + almoco
    trapaceou = False

    for c in consumido:
        if c not in dieta:
            print('CHEATER')
            trapaceou = True
            break
        else:
            dieta = dieta.replace(c, '', 1)
    
    if not trapaceou:
        jantar_ordenado = ''.join(sorted(dieta))
        print(jantar_ordenado)

    # for d in dieta:
    #     if d not in consumido:
    #         jantar += d 
    #     print(sorted(jantar))

