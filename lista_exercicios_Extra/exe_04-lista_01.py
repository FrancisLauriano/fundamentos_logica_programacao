# Lista 01 - Beecrowd

# ENUNCIADO:
# 4. Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. 
# Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

# Entrada
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

# Saída
# O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

# SOLUÇÃO:
N1, N2, N3, N4, N5, N6 = map(float, input('').split())

quantidade = 0
soma = 0

if N1 > 0:
    quantidade += 1
    soma += N1
if N2 > 0:
    quantidade += 1
    soma += N2
if N3 > 0:    
    quantidade += 1
    soma += N3
if N4 > 0:
    quantidade += 1
    soma += N4
if N5 > 0:
    quantidade += 1
    soma += N5
if N6 > 0:
    quantidade += 1
    soma += N6

media = soma / quantidade

print(f'{quantidade} valores positivos')
print('{:.1f}'.format(media))
