# numero = 1

# for c in range(1, 11):
#     print(f'{numero} x {c} = {numero*c}')


for c in range(1, 11):
    for i in range(1, 6):
        print(f'{i} x {c} = {c*i}', end='\t')
    print()

print()

for c in range(1, 11):
    for i in range(6, 11):
        print(f'{i} x {c} = {i*c}', end='\t')
    print()