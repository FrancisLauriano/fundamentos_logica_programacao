def converte_tempo(segundos: int) -> str:
    horas = segundos // 3600
    # resto_seg_1 = segundos % 3600
    minutos = (segundos % 3600) // 60
    seg = (segundos % 3600) % 60

    return f'{horas} : {minutos} : {seg}'

segundos = int(input('Segundos: '))
resultado = converte_tempo(segundos)
print(resultado)