# AULA 8 - Estruturas Condicionais - 12/09/2025
# 1. Faça uma aplicação que receba um nome. Caso esse nome tenha menos de 3 letras ou mais de 12 letras, 
# indique que o nome é inválido.
# Dica: use a função len().

nome = input('informe seu nome: ').sprip()

tamanho = len(nome)

if tamanho < 3 or tamanho > 12:
    print('Nome inválido! Deve conter entre 3 e 12 caracteres.')
else:
    print('Nome válido!')    