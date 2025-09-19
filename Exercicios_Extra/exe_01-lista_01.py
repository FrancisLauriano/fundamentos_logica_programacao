# Lista 01 - Beecrowd

# ENUNCIADO:
# 1. Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. 
# A seguir, calcule e mostre o valor da conta a pagar.

# CÓDIGO   ESPECIFICAÇÃO       PREÇO
# 1        Cachorro Quente     R$ 4.00
# 2        X-Salada           R$ 4.50
# 3        X-Bacon            R$ 5.00
# 4        Torrada simples    R$ 2.00
# 5        Refrigerante       R$ 1.50


# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

# SOLUÇÃO:
codigo, quantidade = map(int, input().split())

if codigo == 1:
    valor = quantidade * 4
elif codigo == 2:
    valor = quantidade * 4.5
elif codigo == 3:
    valor = quantidade * 5
elif codigo == 4:
    valor = quantidade * 2
elif codigo == 5:
    valor = quantidade * 1.5
else:
    pass
    
print('Total: R$ {:.2f}'.format(valor))    
    
    
    