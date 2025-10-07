import random

n = int(input('Escolha um número inteiro de 0 à 10: '))

sorteio = random.randint(0, 10)

tentativas = 1

while n != sorteio:
    print('Não foi dessa vez. Tente novamente!')
    n = int(input('Escolha um número inteiro de 0 à 10: '))
    tentativas += 1

print(f'Você acertou na {tentativas}º tentativa')    


