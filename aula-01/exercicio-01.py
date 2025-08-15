# 1. Faça um algoritmo e um fluxograma que receba um número e indique se ele é impar ou par.

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print(f'O número ${num} é par')
else:
    print(f'O número ${num} é impar')
