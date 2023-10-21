#Librerias utilizadas
from gpiozero import LED
import time


# Definir los LEDs
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)

# Abrir y leer el archivo de texto
with open('input.txt', 'r') as file:
    data = file.read()

# Procesar la solicitud del usuario y encender los LEDs correspondientes
for i in range(4):
    if data[i] == '1':
        if i == 0:
            led1.on()
        elif i == 1:
            led2.on()
        elif i == 2:
            led3.on()
        elif i == 3:
            led4.on()
    else:
        continue

# Esperar un tiempo antes de apagar los LEDs y cerrar el archivo
time.sleep(5)  # Cambia el tiempo a tu preferencia
led1.off()
led2.off()
led3.off()
led4.off()

# Cerrar el archivo
file.close()