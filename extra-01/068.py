import random

maquina_valor = random.randint(0,10)

sua_vitoria = 0

while True:
    seu_valor = int(input('Diga um valor: '))
    sua_escolha = input('Par ou ímpar [P/I] ')

    valor_final = maquina_valor + seu_valor
    print('-'*60)
    

    if valor_final % 2 == 0:
        final_escolha = 'P'
        par_ou_impar = 'PAR'
    else:
        final_escolha = 'I'
        par_ou_impar = 'ÍMPAR'


    print(f'Você jogou {seu_valor} e a máquina jogou {maquina_valor}. Total {valor_final}. É {par_ou_impar}')

    if sua_escolha == final_escolha:
        print('-'*60)
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('-'*60)
        sua_vitoria += 1
    else:
        print('-'*60)
        print('Você perdeu!')
        print('-'*60)
        break
print('Fim')
print(f'Total de vitórias: {sua_vitoria}')
