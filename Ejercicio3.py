from gpiozero import DistanceSensor, LED
import datetime

# Definir los pines GPIO para los LEDs y el sensor ultrasónico
sensor = DistanceSensor(echo=15, trigger=14)
led_red = LED(17)
led_amber = LED(27)
led_green = LED(22)

# Archivo de registro
log_file = "registro_distancias.txt"

# Función para mostrar mensajes y encender los LEDs según la distancia medida
def show_message_and_leds(distance):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"Alerta a las {timestamp}. Distancia: {distance}m\n")
        if distance < 0.1:  # Menos de 10 cm
            file.write("¡Muy cerca!\n")
            led_red.on()
            led_amber.off()
            led_green.off()
        elif distance > 0.3:  # Más de 30 cm
            file.write("¡Excelente!\n")
            led_red.off()
            led_amber.off()
            led_green.on()
        else:  # Entre 10 cm y 30 cm
            file.write("Cerca\n")
            led_red.off()
            led_amber.on()
            led_green.off()

# Bucle principal para medir la distancia continuamente
try:
    while True:
        distance = sensor.distance
        show_message_and_leds(distance)
except KeyboardInterrupt:
    led_red.off()
    led_amber.off()
    led_green.off()