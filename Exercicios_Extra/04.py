# -*- coding: utf-8 -*-

N1, N2, N3 = map(float, input().split())

A = 1.0 
B = 1.0 
C = 1.0

if N1 == N2 and N2 == N3:
    A = N1
    B = N2
    C = N3

else:    
    if N1 >= N2 and N1 >= N3:
        A = N1
        if N2 >= N3:
            B = N2
            C = N3
        else:
            B = N3
            C = N2    
    elif N2 >= N1 and N2 >= N3:
        A = N2
        if N1 >= N3:
            B = N1
            C = N3
        else:
            B = N3
            C = N1
    else:
        A = N3
        if N1 >= N2:
            B = N1
            C = N2
        else:
            B = N2
            C = N1
        
    # if N1 <= N2 and N1 <= N3:
    #     C = N1
    # elif N2 <= N1 and N2 <= N3:
    #     C = N2
    # else:
    #     C = N3
        
    # soma = N1 + N2 + N3
    # B = soma - (A + C)   

    

if A >= (B + C): 
    print('NAO FORMA TRIANGULO')
else:    
    if (A ** 2) == (B ** 2 + C ** 2): 
        print('TRIANGULO RETANGULO')  
    if (A ** 2) > (B ** 2 + C ** 2):   
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < (B ** 2 + C ** 2):     
        print('TRIANGULO ACUTANGULO')     
    if  (A == B) and (B == C):
        print('TRIANGULO EQUILATERO')
    if ((A == B) and (B != C)) or ((B == C) and (C != A)) or ((A == C) and (C != B)):    
        print('TRIANGULO ISOSCELES')
        
    