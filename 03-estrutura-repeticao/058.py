import random 

qtd_palpites = 1

num_sorteio = random.randint(0, 10)

# print(f'NÚMERO SORTEADO: {num_sorteio}\n')

while True:
    num = int(input('Informe um número inteiro entre 0 e 10: '))

    if num != num_sorteio:
        print('\nVocê errou!Tente novamente!\n')
        qtd_palpites += 1
        continue
    else:
        print(f'''{'#'*50}
{f'Parabéns, você acertou na {qtd_palpites}º tentativa!':^50}
{'#'*50}''')
        break
