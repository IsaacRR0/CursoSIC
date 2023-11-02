from flask import Flask
from gpiozero import LED

app = Flask(__name__)

# Inicializar los LEDs en los pines GPIO
leds = [LED(18), LED(23), LED(24)]  

def encender_leds(numero):

    binary = format(numero, '03b')

    for led in leds:
        led.off()
    if binary[0] == '1':
        leds[0].on()
    if binary[1] == '1':
        leds[1].on()
    if binary[2] == '1':
        leds[2].on()

@app.route('/encender/<int:numero>', methods=['GET'])
def encender(numero):
    if 0 <= numero <= 7:  
        encender_leds(numero) 
        return f'Leds encendidos para el número {numero:03b}'
    else:
        return 'Número fuera de rango (debe estar entre 0 y 7)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
