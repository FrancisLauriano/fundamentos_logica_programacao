# AULA 8 - Estruturas Condicionais - 12/09/2025
# 2. Faça um programa que receba 3 números. Caso a soma destes 3 números esteja entre 10 e 20, 
# imprima “Números validados”; caso contrário, imprima “Números inválidos”.

num1, num2, num3 = map(float, input('Infome três números: ').split())

soma = num1 + num2 + num3

if soma >= 10 and soma <= 20:
    print('Números válidos')
else:
    print('Números inválidos')    