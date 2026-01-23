def cinco_colocado(classificacao: tuple) -> str:
    resultado = f'Os cinco primeiros colocados são:\n'
    for posicao, time in enumerate(classificacao[:5]):
        resultado += f'{posicao + 1}º - {time}\t'
    return resultado

def quatro_ultimos(classificacao: tuple) -> str:
    resultado = f'Os quatro ultimos colocados são:\n'
    for posicao, time in enumerate(classificacao[-4:], start=len(classificacao) - 3):
        resultado += f'{posicao}º - {time}\t'
    return resultado

def ordem_alfabetica_times(classificacao: tuple) -> str:
    resultado = f'Times por ordem aflfabetica:\n'
    ordem_alfabetica = sorted(classificacao)

    for time in ordem_alfabetica:
        resultado += f'{time}\n' 
    
    return resultado

def posicao_de_um_time(classificacao, time: str) -> str:
    for posicao, nome_time in enumerate(classificacao):
        if nome_time == time:
            return f'O {nome_time} está na {posicao + 1}º posição'
    return f'{time} não está entre os 10º colocados'


def brasileirao_futebol(classificacao, time): 
    print(cinco_colocado(classificacao))
    print()
    print(quatro_ultimos(classificacao))
    print()
    print(ordem_alfabetica_times(classificacao))
    print()
    print(posicao_de_um_time(classificacao, time))

classificacao = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco')
time = input('Nome do time: ').capitalize().strip()
print(brasileirao_futebol(classificacao, time))



# dado = input('Digite a classificação: ')
# classificacao = tuple(dado.split(','))
# classificacao = tuple(input('Digite a classificação: ').split(','))
# classificacao = 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco'
# time = input('Nome do time: ').capitalize()



# print(cinco_colocado(classificacao))
# print()
# print(quatro_ultimos(classificacao))
# print()
# print(ordem_alfabetica_times(classificacao))
# print()
# print(posicao_de_um_time(classificacao, time))


# 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco'

