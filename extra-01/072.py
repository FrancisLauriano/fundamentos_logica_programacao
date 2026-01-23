def contagem_ate_vinte(numero: int) -> str:
    contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


    return contagem[numero]
      
numero = -1

while True:
    numero = int(input('Digite um valor: '))
    if numero < 0 or numero > 20:
        print('Valor Inválido')
    else:
        valor = contagem_ate_vinte(numero)
        print(valor)
        break
    
