# -*- coding: utf-8 -*-
import math

G = 9.80665
PI = 3.14159 

while True:
    try:
        h = float(input())
        p1, p2 = map(int, input().split())
        n = int(input())
    # EOFError
    except EOFError:
        break
    
    for i in range(0, n):
        alfa, v = map(float, input().split())
        
        radiano = alfa * (PI/180)
        vx = v * math.cos(radiano)
        vy = v * math.sin(radiano)
        raiz = ((vy**2) + (2 * G * h))**(1/2)
        tempo_total = (vy + raiz) / G
        alcance_horizontal = vx * tempo_total

        
        if alcance_horizontal >= p1 and alcance_horizontal <= p2:
            acerto = 'DUCK'
        else:
            acerto = 'NUCK'
            
        print('{:.5f} -> {}'.format(alcance_horizontal, acerto))
