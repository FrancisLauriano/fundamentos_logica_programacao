import datetime

qtd_maiores = 0
qtd_nao_maiores = 0
ano_atual = datetime.date.today().year

for c in range(1, 8):
    ano = int(input('Ano: '))

    if ano_atual - ano >= 18:
        qtd_maiores += 1
    else:
        qtd_nao_maiores += 1

print(f'Maiores: {qtd_maiores} Menores: {qtd_nao_maiores}')

