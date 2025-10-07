# -*- coding: utf-8 -*-

N = int(input('Digite número: '))

i = 1

# if N > 2 and N < 1000:
#     for i in range(1, 11):
#         print(f'{i} X {N} = {i*N}')
#         i += 1


while (i <= 10) and (N > 2 and N < 1000):
    print(f'{i} X {N} = {i*N}')
    i += 1   