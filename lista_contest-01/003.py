testes = int(input('Teste: '))

for i in range(1, testes+1):
    frase = input('Infome a frase: ')

    palavra1, palavra2 = frase.split()

    nova_palavra = ' '

    i = 0 
    while i < len(palavra1) or i < len(palavra2):
        if i < len(palavra1):
            nova_palavra += palavra1[i]
        if i <len(palavra2):
            nova_palavra += palavra2[i]

        i += 1
    
    print(nova_palavra)

