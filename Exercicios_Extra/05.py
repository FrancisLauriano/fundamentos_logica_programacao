# -*- coding: utf-8 -*-

hora_inicial, min_inicial, hora_final, min_final = map(int, input().split())

min_total_inicial = (hora_inicial * 60) + min_inicial
min_total_final  = (hora_final * 60) + min_final

duracao_total_em_min = min_total_final - min_total_inicial
hora_duracao = duracao_total_em_min // 60
min_duracao = duracao_total_em_min % 60

if duracao_total_em_min < 0:
    duracao_total_em_min = (min_total_final + (24 * 60)) - min_total_inicial
    hora_duracao = duracao_total_em_min // 60
    min_duracao = duracao_total_em_min % 60
elif hora_inicial == hora_final and  min_inicial == min_final:
    hora_duracao = 24
    min_duracao = 0
    
print(f'O JOGO DUROU {hora_duracao} HORA(S) E {min_duracao} MINUTO(S)')    
    
    



    
       