nome = input('Digite seu nome: ')

tamanho = len(nome)

if tamanho > 20:
    print(f'[ERRO] Mais de 20 caracteres. {tamanho} caracteres')
else:
    print(f'Operação Válida. {tamanho} caracteres')    