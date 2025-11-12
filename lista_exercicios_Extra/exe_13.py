# AULA 8 - Estruturas Condicionais - 12/09/2025
# 4. Faça um programa que receba um número inteiro. Caso o número digitado seja ímpar e 
# esteja entre 30 e 50, então imprima “acertou”; caso contrário, imprima “errou”.

num = int(input('Informe um número inteiro: '))

if (num % 2 != 0) and (num >= 30 and num <= 50):
    print('Acertou')
else:
    print('Errou')   