def contador_leds(numeracao: str) -> int:

    leds = 0

    for digito in numeracao:
        # if digito == '1':
        #     leds += 2
        # elif digito == '2':
        #     leds += 5
        # elif digito == '3':
        #     leds += 5
        # elif digito == '4':
        #     leds += 4
        # elif digito == '5':
        #     leds += 5
        # elif digito == '6':
        #     leds += 6
        # elif digito == '7':
        #     leds += 3
        # elif digito == '8':
        #     leds += 7
        # elif digito == '9':
        #     leds += 6
        # elif digito == '0':
        #     leds += 6

        # OU 

        match digito:
            case '1':
                leds += 2
            case '2':
                leds += 5
            case '3':
                leds += 5
            case '4':
                leds += 4
            case '5':
                leds += 5
            case '6':
                leds += 6
            case '7':
                leds += 3
            case '8':
                leds += 7
            case '9':
                leds += 6
            case '0':
                leds += 6
            


    return leds

teste = int(input('Número inteiro: '))

for i in range(1, teste + 1):
    numero = str(input('Infome a numeração: ')).strip()
    resultado_leds = contador_leds(numero)
    print(f'{resultado_leds} leds')