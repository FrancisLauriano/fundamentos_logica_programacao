def fatorial(numero: int):
    fatorial = 1
    sequencia = ''
    if numero == 0 or numero == 1:
        return f'{numero}! = 1'
    else:
        for i in range(1, numero + 1):
            fatorial *= i
            sequencia += str(i)

            if i >= 1:
                sequencia += ' . '

        return f'{numero}! = {sequencia} = {fatorial}'
    
numero = int(input('Informe um número inteiro: '))
resultado = fatorial(numero)
print(resultado)
