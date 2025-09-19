# Lista 01 - Beecrowd

# ENUNCIADO:
# 5. Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

# SOLUÇÃO:
N1, N2, N3, N4, N5 = map(int, input('').split())

quantidade = 0

if N1 % 2 == 0:
    quantidade += 1
if N2 % 2 == 0:
    quantidade += 1
if N3 % 2 == 0:    
    quantidade += 1
if N4 % 2 == 0:
    quantidade += 1
if N5 % 2 == 0:
    quantidade += 1

print(f'{quantidade} valores pares')