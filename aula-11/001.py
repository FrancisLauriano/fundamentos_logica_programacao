palavra = input('Digite palavra: ')
# palavra = input('Digite palavra: ').lower()

for letra in palavra:
    if letra not in 'aeiouAEIOU':
    # if letra != 'a' and letra !='e' and letra != 'i' and letra != 'o' and letra != 'u':
        print(letra)
    