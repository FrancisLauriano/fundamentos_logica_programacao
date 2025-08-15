# 3.Determinado jovem decide realizar uma viagem, faça o algoritmo e o fluxograma do processo.
# obs.1: leve em consideração todo o processo desde a tomada de decisão de viajar.
# obs.2: apenas considere a ida da viagem, desconsidere a volta e estadia.

resposta = int(input('Deseja viajar?\n[1. SIM] [2. NÃO]: '))

if resposta != 1:
    print(f'Viagem cancelada')
else:
    print(f'1. Escolher Destino')
    print(f'2. Defenir data de viagem')
    print(f'3. Comprar passagem')
    print(f'4. Reservar Hotel/ Pousada')
    print(f'5. Separar documentos e passagens')
    print(f'6. Arrumar as malas')
    print(f'7. Ir ao aeroporto')
    print(f'8. Realizar check-in')
    print(f'9. Realizar embarque')
    print(f'10. Chegar ao destino')