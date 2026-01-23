import random

def aleatorio():
    numeros_tuple = ()

    for c in range(5):
        numero = random.randint(1, 100)
        numeros_tuple += (numero,)

    maior = numeros_tuple[0]
    menor = numeros_tuple[0]

    for numero in numeros_tuple:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return f'Numeros: {numeros_tuple}\nMaior número: {maior} | Menor número: {menor}'
        

print(aleatorio())


