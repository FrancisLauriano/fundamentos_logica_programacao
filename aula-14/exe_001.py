def paridade(numero: int) -> int:
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
def num_perfeito(numero: int) -> int:
    soma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    
    if soma_divisores == numero:
        return 'É Perfeito'
    else:
        return 'Não é Perfeito'
    
def num_primo(numero: int) -> int:
    qtd_divisores = 0

    # não existe divisores de n maior que n/2
    for i in range(1, (numero // 2) + 1):
        if numero % i == 0:
            qtd_divisores += 1
    
    qtd_divisores += 1 # soma 1 pq todo numero é divisivel por ele mesmo

    if qtd_divisores == 2:
        return 'É Primo'
    else:
        return 'Não é Primo'


    



  