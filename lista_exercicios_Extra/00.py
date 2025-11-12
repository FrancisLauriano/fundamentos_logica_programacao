import random

tent_um = int(input("Digite um número entre 1 e 10: "))

sorteio = random.randint(1,10)

if tent_um == sorteio:
    print("Parabéns! Você acertou o número sorteado.")
else:
    print(f"Que pena! Você errou. Tente novamente.")    

    tent_dois = int(input("Digite um número entre 1 e 10: "))
    if tent_dois == sorteio:
        print("Parabéns! Você acertou o número sorteado.")
    else:
        print(f"Que pena! Você errou novamente. Tente novamente")

        tent_tres = int(input("Digite um número entre 1 e 10: "))

        if tent_tres == sorteio:
            print("Parabéns! Você acertou o número sorteado.")  
        else:
            print(f"Que pena! Você errou novamente. Tente novamente")

            tent_quatro = int(input("Digite um número entre 1 e 10: "))

            if tent_quatro == sorteio:
                print("Parabéns! Você acertou o número sorteado.")
            else:
                print(f"Que pena! Você errou novamente. O número sorteado era {sorteio}.")

print("Fim do jogo.")