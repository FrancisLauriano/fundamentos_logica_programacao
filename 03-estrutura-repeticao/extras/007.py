n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))


menor = n1

if n2 < menor:
    menor = n2
    
produto = 1
fator = ''

while n1 > 1 and n2 > 1:
    
    for c in range(2, menor):
        while n1 % c == 0 or n2 % c == 0:
            if n1 % c == 0 and n2 % c == 0:
                fator += f'{c}.'
                produto *= c
                print(f'{int(n1)}, {int(n2)} | {c}')
                n1 /= c
                n2 /= c
            elif n1 % c == 0 and n2 % c != 0:
                fator += f'{c}.'
                produto *= c
                print(f'{int(n1)}, {int(n2)} | {c}')
                n1 /= c
            elif n2 % c == 0 and n1 % c != 0: 
                fator += f'{c}.'
                produto *= c
                print(f'{int(n1)}, {int(n2)} | {c}')
                n2 /= c
print(f'{int(n1)}, {int(n2)} | {fator} = {produto}')