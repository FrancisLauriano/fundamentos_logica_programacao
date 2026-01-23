import datetime

ano_atual = datetime.datetime.now().year

qtd_maior = 0

# print(ano_atual)

for c in range(1, 8):
    ano_nascimento = int(input(f'Informe o ano de nascimento na {c}º pessoa: '))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        qtd_maior += 1

print(f'{qtd_maior} são maiores de idade.\n{7 - qtd_maior} são menores de idade')

