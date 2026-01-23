frase = input('Digite frase: ').strip().lower()

qtd_a = frase.count('a')
print(f'Quantidade letra "a" em {frase}: {qtd_a}')

primeiro_a = frase.find('a')
print(f'Primeiro: {primeiro_a}')

ultimo_a = frase.find('a', -1)
print(f'Ultima: {ultimo_a}')

