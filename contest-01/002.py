frase = input('Infome frase: ')

frase_nova = ''
c = 0

for letra in frase:
    if letra != ' ':
        if c % 2 == 0:
            frase_nova += letra.upper()
        else:
            frase_nova += letra.lower()
        c += 1
    else: 
        frase_nova += letra

print(frase_nova)


    

    
