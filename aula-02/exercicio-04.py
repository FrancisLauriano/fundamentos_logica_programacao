# 4. Faça o algoritmo do MDC usando a solução tradicional e o algoritmo de Euclides.
# 1.Receber o número n1
# 2.Receber o número n2
# 3.Enquanto o resto da divisão de n1 por n2 for maior que zero:
# -> R = resto da divisão de n1 por n2
# -> n1 = n2
# -> n2 = R
# 4. Resposta n2


# Tradicional:
def mdc_tradicional(n1, n2):
    # normalizar sinais (sem usar an2s)
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2

    # tratar zeros
    if n1 == 0 and n2 == 0:
        return 0   # ou levantar erro, conforme a sua convenção
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    # achar o menor sem min()
    if n1 < n2:
        menor = n1
    else:
        menor = n2

    mdc = 1
    i = 1
    while i <= menor:
        if n1 % i == 0 and n2 % i == 0:
            mdc = i
        i = i + 1   # precisa estar dentro do while
    return mdc


# Programa principal - Método Tradicional
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado_mdc_tradicional = mdc_tradicional(n1, n2)
print("O MDC entre - Método Tradicional", n1, "e", n2, "é:", resultado_mdc_tradicional)


# Algoritmo de Euclides:
def mdc_euclides(n1, n2):
    # normalizar sinais (sem usar an2s)
    if n1 < 0:
        n1 = -n1
    if n2 < 0:
        n2 = -n2

    # tratar zeros
    if n1 == 0 and n2 == 0:
        return 0   # ou levantar erro, conforme n1 sua convenção
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    while n2 != 0:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    return n1

# Programa principal - Método de Euclides
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

resultado_mdc_euclides = mdc_euclides(n1, n2)
print("O MDC entre - Método Euclides", n1, "e", n2, "é:", resultado_mdc_euclides)