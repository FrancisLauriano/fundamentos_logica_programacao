nome = input('Digite nome: ').lower().strip()

verifica_nome = nome.find('silva')

if verifica_nome != -1:
    print(f'{nome} tem "silva"')
else:
    print(f'{nome} não tem "silva"')