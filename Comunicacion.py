import paho.mqtt.client as mqtt
import time

# Configuración de conexión MQTT
mqtt_broker = "broker.mqtt-dashboard.com"  # Cambia esto por la dirección de tu broker MQTT
mqtt_port = 1883
mqtt_topic = "raspberrypi"  # Elige un tema MQTT relevante

# Inicialización de cliente MQTT
client = mqtt.Client("RPI")
client.connect(mqtt_broker, mqtt_port)

# Función para enviar datos
def enviar_mensaje(mensaje):
    client.publish(mqtt_topic, mensaje)
    print("Mensaje enviado: " + mensaje)

# Función de recepción de mensajes
def on_message(client, userdata, message):
    print("Mensaje recibido: " + message.payload.decode())

client.on_message = on_message
client.subscribe(mqtt_topic)
client.loop_start()

# Ejemplo de uso
enviar_mensaje("Hola desde Raspberry Pi")

# Mantén el programa en funcionamiento
while True:
    time.sleep(1)
