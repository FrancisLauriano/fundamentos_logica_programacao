soma = 0
lista_pares = []
for i in range (0, 6):
    n = int(input(f'Digite o {i+1}º número: '))
    
    if n % 2 == 0:
        soma += n
        lista_pares.append(n)
        

print(f'Soma dos pares {lista_pares} é: {soma}')
print('Fim')    