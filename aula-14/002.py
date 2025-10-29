def area_triangulo(base: float, altura: float) -> float:
    area = (base * altura) / 2
    return area


def area_retangulo(base: float, altura: float) -> float:
    area = base * altura
    return area

base, altura = map(float, input('Informe a base e altura: ').split())
resultado = area_triangulo(base, altura)
print('A área do triangulo é {:.2f}'.format(resultado))