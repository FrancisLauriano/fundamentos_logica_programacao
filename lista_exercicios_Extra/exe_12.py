# AULA 8 - Estruturas Condicionais - 12/09/2025
# 3. Faça uma aplicação que receba 3 números quaisquer e, independentemente da ordem em que forem digitados, 
# imprima-os no formato: “menor < médio < maior”.


num1, num2, num3 = map(float, input('informe três números:').split())

maior = 0
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

menor = 0
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

medio = (num1 + num2 + num3) - (maior + menor)

print(f'{menor} < {medio} < {maior}')        