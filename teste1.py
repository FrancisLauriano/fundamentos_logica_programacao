import RPi.GPIO as GPIO
import time

# Configuração inicial
GPIO.setmode(GPIO.BCM)

# Pinos dos LEDs
vermelho = 18
amarelo = 23
verde = 24

# Pino do botão
botao = 25

# Configuração dos pinos
GPIO.setup(vermelho, GPIO.OUT)
GPIO.setup(amarelo, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(botao, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Estado inicial
semaforo_ligado = False

def sequencia_semaforo():
    """Executa a sequência completa do semáforo."""
    GPIO.output(verde, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(verde, GPIO.LOW)

    GPIO.output(amarelo, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(amarelo, GPIO.LOW)

    GPIO.output(vermelho, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(vermelho, GPIO.LOW)

def alternar_estado(channel):
    """Alterna o estado do semáforo (liga/desliga) quando o botão é pressionado."""
    global semaforo_ligado
    semaforo_ligado = not semaforo_ligado  # inverte o estado atual
    if semaforo_ligado:
        print("Semáforo LIGADO")
    else:
        print("Semáforo DESLIGADO (todos LEDs apagados)")
        GPIO.output(vermelho, GPIO.LOW)
        GPIO.output(amarelo, GPIO.LOW)
        GPIO.output(verde, GPIO.LOW)

# Configura o evento de detecção com DEBOUNCE (200 ms)
GPIO.add_event_detect(botao, GPIO.RISING, callback=alternar_estado, bouncetime=200)

try:
    print("Sistema pronto. Pressione o botão para alternar o semáforo.")

    while True:
        if semaforo_ligado:
            sequencia_semaforo()
        else:
            time.sleep(0.1)  # reduz uso de CPU quando está desligado

except KeyboardInterrupt:
    print("\nEncerrando programa...")
    GPIO.cleanup()
