N1 = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())
N5 = int(input())

positivos = 0
negativos = 0
pares = 0
impares = 0

if N1 > 0:
    positivos += 1
elif N1 < 0:
    negativos += 1
if N2 > 0:
    positivos += 1
elif N2 < 0:
    negativos += 1    
if N3 > 0:
    positivos += 1
elif N3 < 0:
    negativos += 1    
if N4 > 0:
    positivos += 1
elif N4 < 0:
    negativos += 1    
if N5 > 0:
    positivos += 1
elif N5 < 0:
    negativos += 1    

if N1 % 2 == 0:
    pares += 1
else:
    impares += 1  
if N2 % 2 == 0:
    pares += 1
else:
    impares += 1     
if N3 % 2 == 0:
    pares += 1
else:
    impares += 1      
if N4 % 2 == 0:
    pares += 1
else:
    impares += 1      
if N5 % 2 == 0:
    pares += 1
else:
    impares += 1      
    
print(f'{pares} valor(es) par(es)') 
print(f'{impares} valor(es) impar(es)')  
print(f'{positivos} valor(es) positivo(s)') 
print(f'{negativos} valor(es) negativo(s)')     
    
    
    
    
    