import random

acerto = 0

while True:
    pc = random.randint(0, 10)

    num = int(input('Informe um valor inteiro: '))

    while True:
        escolhe = input('Par ou Ímpar [P | I]: ').lower()

        if escolhe != 'p' and escolhe != 'i':
            print('Opção Inválida. Tente novamente!\n')
            continue
        else:
            soma = pc + num

            if soma % 2 == 0:
                valor = 'p'
                resultado = 'PAR'
            else:
                valor = 'i'
                resultado = 'ÍMPAR'

            print(f'Você jogou {num} e computador jogou {pc}. Total: {soma}. Deu {resultado}')
            break

    if escolhe == valor:
        acerto += 1
        print(f'''Você venceu! Vamos jogar novamente...\n''')
        continue
    else:
        print(f'Você errou! Você acertou {acerto} vezes\n')
        break 
        

