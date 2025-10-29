def baskara(A: int, B: int, C: int):
    if A == 0:
        return 'Não é função do segundo grau'
    else:
        delta = (B**2) - (4 * A * C)

        if delta < 0:
            return 'Não existe raizes reais'
        elif delta == 0:
            raiz = - B / (2 * A)
            return raiz
        else:
            raiz_1 = (- B + (delta)) / (2 * A)
            raiz_2 = (- B - (delta)) / (2 * A)
            return raiz_1, raiz_2
        
A, B, C = map(int, input('Informe A, B e C: '). split())
resultado = baskara(A, B, C)
print(f'{resultado}')