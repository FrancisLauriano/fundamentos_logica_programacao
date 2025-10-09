import datetime

ano_atual = datetime.date.today().year
# print(ano_atual)

maiores = 0
nao_maiores = 0

for i in range(1, 8):
    ano_nasc = int(input('Informe ano nascimento: '))

    idade = ano_atual - ano_nasc

    if idade >= 18:
        maiores += 1
    else:
        nao_maiores += 1

print(f'{maiores} pessoas maiores de idade')
print(f'{nao_maiores} pessoas ainda não atigiram a maior idade')
