import datetime

ano_atual = datetime.date.today().year
# print(ano_atual)

qtd_maiores = 0

for c in range(0, 7):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {c+1}º pessoa: '))

    if (ano_atual - ano_nascimento) >= 18:
        qtd_maiores += 1
print(f'{qtd_maiores} pessoas são maiores de idade')        