nome = input('Digite nome: ').strip()

separa_nome = nome.split()

primeiro_nome = separa_nome[0]
print(f'Primeiro nome: {primeiro_nome}')

ultimo_nome = separa_nome[-1]
print(f'Ultimo nome: {ultimo_nome}')
