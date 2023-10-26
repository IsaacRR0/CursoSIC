import paho.mqtt.client as mqtt

broker_address = "192.168.0.25"  
puerto = 1883
cliente = mqtt.Client("RaspberryPi")

def on_message(client, userdata, message):
    mensaje = message.payload.decode('utf-8')
    print(f"Mensaje recibido: {mensaje}")

cliente.connect(broker_address, puerto)
cliente.subscribe("topic/ejemplo")  

cliente.on_message = on_message

cliente.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

cliente.disconnect()