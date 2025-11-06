def divisao_inteira(numerador, denominado):
    if numerador < denominado:
        return 0
    else:
        return 1 + divisao_inteira(numerador - denominador, denominador)

