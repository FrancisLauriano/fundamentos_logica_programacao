n1, n2 = map(int, input('Digite dois números: ').split())

fator = 2
mmc = 1

while n1 > 1 or n2 > 1:

    if n1 % fator == 0 and n2 % fator == 0:
        print(f'{n1:3} {n2:3} | {fator}')
        n1 //= fator
        n2 //= fator
        mmc *= fator
    
    elif n1 % fator == 0:
        print(f'{n1:3} {n2:3} | {fator}')
        n1 //= fator
        mmc *= fator

    elif n2 % fator == 0:
        print(f'{n1:3} {n2:3} | {fator}')
        n2 //= fator
        mmc *= fator

    else:
        fator += 1

print('-'*15)
print(f'{1:3} {1:3} | MMC: {mmc}')




