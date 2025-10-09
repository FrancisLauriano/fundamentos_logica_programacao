import random

sorteio = random.randint(1, 10)

while True:
    numero = int(input('\nInforme um número inteiro: '))

    if numero == sorteio:
        break
    
    print('Você errou! Tente novamente!')

print('Você acertou!')