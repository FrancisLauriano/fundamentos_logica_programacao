# -*- coding: utf-8 -*-

N = int(input('digite: '))
# quadrado = 0

i = 1

while (i <= N) and (N > 5 and N < 2000):
    if i % 2 == 0:
        print(f'{i}^2 = {i**2}')
    i += 1