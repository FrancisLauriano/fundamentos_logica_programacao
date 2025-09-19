# -*- coding: utf-8 -*-

N1, N2, N3 = map(float, input().split())

A = 0.0 
B = 0.0 
C = 0.0

if N1 >= N2 and N1 >= N3:
    A = N1
elif N2 >= N1 and N2 >= N3:
    A = N2
else:
    A = N3
    
if N1 <= N2 and N1 <= N3:
    C = N1
elif N2 <= N1 and N2 <= N3:
    C = N2
else:
    C = N3
    
soma = N1 + N2 + N3
B = soma - (A + C)
    

if A >= (B + C): 
    print('NAO FORMA TRIANGULO')
else:    
    if (A**2) == (B**2 + C**2): 
        print('TRIANGULO RETANGULO')  
    elif (A**2) > (B**2 + C**2):   
        print('TRIANGULO OBTUSANGULO')
    elif (A**2) < (B**2 + C**2):     
        print('TRIANGULO ACUTANGULO')
            
    if  (A == B) and (B == C):
        print('TRIANGULO EQUILATERO')
    elif (A == B) or (B == C) or (A == C):    
        print('TRIANGULO ISOSCELES')
        
    