# Velocidade = Distância / Tempo
# Distância = Velocidade * Tempo
# Tempo = Distância / Velocidade

# MRU (movimento retilíneo uniforme): ambos os barcos têm velocidade constante (sem aceleração, sem correnteza/vento).

# Referencial e eixos: tomamos a costa como eixo 𝑥 (horizontal) e o mar aberto como eixo y (vertical).
# – O fugitivo parte do ponto (0,0) e navega perpendicularmente à costa: seu movimento é ao longo do eixo 𝑦. 
# – A Guarda parte do ponto (D,0), na própria costa, a D milhas náuticas lateralmente do ponto de fuga.
# Como o fugitivo vai reto para o alto-mar, sua posição é: rf​(t)=(0,Vf​t).
# No instante t, ele terá avançado yf = Vft milhas para dentro do mar.
# Ele escapa se alcançar 𝑦𝑓 = 12 y, o que ocorre no tempo: tescape​ = 12 / Vf. 

# Se a interceptação ocorre no instante t, os dois barcos estão no mesmo ponto (x,y).
# Como o fugitivo permanece sobre a reta x=0, o ponto de encontro tem coordenadas (0, Vft).
# A Guarda sai de (D,0) e precisa chegar a (0, Vft). A trajetória mais rápida em MRU é uma reta (qualquer curva aumenta o caminho), cujo comprimento é a hipotenusa do triângulo formado por:
# cateto horizontal: D
# cateto vertical: Vft
# Logo, a distância que a Guarda percorre até o encontro é: L(t)= (D**2+(Vft)**2)**1/2. 
# Como ela navega com velocidade constante Vg, o tempo gasto para percorrer L(t) é exatamente t. Então: Vgt=L(t)=(D**2+(Vft)**2)**1/2
# Equação do encontro e condição de possibilidade. Elevando ao quadrado:
# (Vg**2) * (t**2)=D**2 + (Vf**2) * (t**2) ⇒t**2(Vg**2−Vf2**2)=D**2.
# Daí:
# t= D / ((Vg**2 – Vf**2)**1/2)
# Comparação de tempos (princípio de decisão)
# Há dois relógios concorrendo:
# Relógio da fuga: tescape=12/Vft (tempo para o fugitivo atingir 12 milhas).
# Relógio da interceptação: tintercept= D / (Vg**2−Vf**2) (tempo mínimo para a Guarda alcançar o fugitivo).
# Conclusão física/matemática:
# Se Vg ≤ Vf → interceptação impossível.
# Se Vg > Vf, comparamos:
#   tintercept ≤ tescape :    D / (Vg**2−Vf**2)  ≤ 12/Vft  


D, VF, VG = map(float, input('Informe valores: ').split())





