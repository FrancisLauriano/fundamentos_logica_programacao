import RPi.GPIO as GPIO
import time

# Pinos GPIO
BOTAO_PIN = 16
VERMELHO = 18
AMARELO = 23
VERDE = 24

# Estado inicial do semáforo
semaforo_ligado = False
prev_button_state = GPIO.LOW
button_state = GPIO.LOW

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setup([VERMELHO, AMARELO, VERDE], GPIO.OUT)
GPIO.setup(BOTAO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def apagar_todos():
    GPIO.output(VERMELHO, GPIO.LOW)
    GPIO.output(AMARELO, GPIO.LOW)
    GPIO.output(VERDE, GPIO.LOW)

def sequencia_semaforo():
    GPIO.output(VERDE, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(VERDE, GPIO.LOW)

    GPIO.output(AMARELO, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(AMARELO, GPIO.LOW)

    GPIO.output(VERMELHO, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(VERMELHO, GPIO.LOW)

try:
    while True:
        prev_button_state = button_state
        button_state = GPIO.input(BOTAO_PIN)

        # Detecta transição (botão pressionado)
        if prev_button_state == GPIO.HIGH and button_state == GPIO.LOW:
            time.sleep(0.1)  # debounce de 100 ms
            semaforo_ligado = not semaforo_ligado
            print("Semáforo LIGADO" if semaforo_ligado else "Semáforo DESLIGADO")
            if not semaforo_ligado:
                apagar_todos()

        # Executa a sequência se estiver ligado
        if semaforo_ligado:
            sequencia_semaforo()
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nEncerrando programa...")
    apagar_todos()
    GPIO.cleanup()
