
primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))

total_termo = 10

ultimo_termo = primeiro + (razao * total_termo)

while total_termo != 0:
    for c in range(primeiro, ultimo_termo, razao): 
        print(f'{c}, ', end='')
        
    total_termo = int(input('\nQuantos mais termos deseja? '))
    primeiro = ultimo_termo
    ultimo_termo = primeiro + (razao * total_termo)
         

#####################################################
    
        
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

mais_termo = 10
total_termo = 0

while mais_termo != 0:

    total_termo += mais_termo

    while total_termo > 0:
        print(f'{primeiro}, ', end='')
        primeiro += razao
        total_termo -= 1

    mais_termo = int(input('\nQuantos mais termos deseja? '))





