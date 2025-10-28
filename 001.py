def soma_termos(termos:int) -> int:
    soma = 0
    for i in range(1, termos+1):
        soma += i
    return soma

numero = int(input('Digite um valor: '))
resultado_soma = soma_termos(numero)
print(f'Resultado da soma dos N-Termos: {resultado_soma}')

