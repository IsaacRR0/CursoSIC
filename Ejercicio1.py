import datetime
from gpiozero import Button

button_pin = 17
log_file = "Registro de tiempo.txt"
button = Button(button_pin)

try:
    while True:
        button.wait_for_press()
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as file:
            file.write(date_time + "\\n")
        print("Botón presionado. Fecha y hora escritas en el archivo.")

except KeyboardInterrupt:
    pass