# 3. Faça um algorítimo que calcule as raízes da equação de baskara.

# "ax2+bx+c=0"

#  x = (-b ± √Δ) / 2a

valorA = int(input('Inserir o valor de A: '))
valorB = int(input('Inserir o valor de B: '))
valorC = int(input('Inserir o valor de C: '))

if valorA == 0:
    print(f'Não é uma equação do segundo grau')
else:    
    delta = (valorB*valorB)-4*valorA*valorC

    if delta < 0:
        print(f'Não existe raizes reais')

