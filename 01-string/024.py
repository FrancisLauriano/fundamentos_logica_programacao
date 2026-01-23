cidade = input('Digite a cidade: ').lower().strip()

verifica_cidade = cidade.find('santo')

if verifica_cidade == 0:
    print(f'{cidade} começa com "santo"')
else:
    print(f'{cidade} não começa com "santo"')