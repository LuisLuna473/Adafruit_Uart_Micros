# Import standard python modules.
import sys
import time
import random
import serial


# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient

# holds the count for the feed


ADAFRUIT_IO_USERNAME = "Luis473"
ADAFRUIT_IO_KEY      = "aio_zbOF568nHykysUr18GXpaCa5DL03" 

# Set to the ID of the feed to subscribe to for updates.
#feedContador = 'contador'
feedServ1 = 'serv1'
feedServ2 = 'serv2'
feedServ3 = 'serv3'
feedServ4 = 'serv4'
feedPush1 = 'push1'
feedPush2 = 'push2'
feedPush3 = 'push3'
feedTemperatura = 'temperatura'

mensaje = ''
cadena_mc = ''

# Define callback functions which will be called when certain events happen.
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    #print('Subscribing to Feed {0} and {1}'.format(feedLed, feedContador))
    client.subscribe(feedServ1)
    client.subscribe(feedServ2)
    client.subscribe(feedServ3)
    client.subscribe(feedServ4)
    client.subscribe(feedPush1)
    client.subscribe(feedPush2)
    client.subscribe(feedPush3)
    print('Waiting for feed data...')

def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)

def update_servo_values(feed_id, payload):
    global cadena_mc
    
    # Control para imprimir la cadena actual antes de dividirla
    print("Cadena actual:", cadena_mc.strip())
    
    # Dividir la cadena actual en una lista de pares clave-valor
    if cadena_mc.strip() == "":
        servo_values = []
    else:
        servo_values = [pair.split(':') for pair in cadena_mc.strip().split(',')]
    
    # Actualizar el valor del servo correspondiente
    found = False
    for index, item in enumerate(servo_values):
        if len(item) == 2:
            key, value = item[0].strip(), item[1].strip()
            if key == f'ser{feed_id[-1]}':
                servo_values[index][1] = payload
                found = True
                break
    
    if not found:
        # Si el servo correspondiente no se encontró en la cadena, agregarlo
        servo_values.append([f'ser{feed_id[-1]}', payload])
    
    # Volver a concatenar la cadena actualizada sin espacios
    cadena_mc = ','.join([f'{key}:{value}' for key, value in servo_values if len(key) > 0 and len(value) > 0])

    print("Cadena actualizada:", cadena_mc)

def message(client, feed_id, payload):
    global cadena_mc 
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    
    if (feed_id == feedServ1 or feed_id == feedServ2 or feed_id == feedServ3 or feed_id == feedServ4):
        "Lista de caracteres a = serv1, b= serv2, c = serv3, d= serv4"

        if (feed_id == feedServ1): 
            arduino.write(bytes('a\n', 'utf-8'))
            time.sleep(0.1)
        if (feed_id == feedServ2):
            arduino.write(bytes('b\n', 'utf-8'))
            time.sleep(0.1)
        if (feed_id == feedServ3):
            arduino.write(bytes('c\n', 'utf-8'))
            time.sleep(0.1)
        if (feed_id == feedServ4):
            arduino.write(bytes('d\n', 'utf-8'))
            time.sleep(0.1)
        
        if(payload == 0):
            print("Valor nuevo:", payload)
            arduino.write(bytes('e\n', 'utf-8'))
            time.sleep(0.1)
        if(payload == 10):
            print("Valor nuevo:", payload)
            arduino.write(bytes('f\n', 'utf-8'))
            time.sleep(0.1)
        if(payload == 20): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('g\n', 'utf-8'))
        if(payload == 30): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('h\n', 'utf-8'))
        if(payload == 40): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('i\n', 'utf-8'))
        if(payload == 50): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('j\n', 'utf-8'))
        if(payload == 60): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('k\n', 'utf-8'))
        if(payload == 70): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('l\n', 'utf-8'))
        if(payload == 80): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('m\n', 'utf-8'))
        if(payload == 90): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('n\n', 'utf-8'))
        if(payload == 100): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('o\n', 'utf-8'))
        if(payload == 120): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('p\n', 'utf-8'))
        if(payload == 130): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('q\n', 'utf-8'))
        if(payload == 140): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('r\n', 'utf-8'))
        if(payload == 150): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('s\n', 'utf-8'))
        if(payload == 160): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('t\n', 'utf-8'))
        if(payload == 170): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('u\n', 'utf-8'))
        if(payload == 180): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('v\n', 'utf-8'))
        if(payload == 190): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('w\n', 'utf-8'))
        if(payload == 200): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('x\n', 'utf-8'))
        if(payload == 210): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('y\n', 'utf-8'))
        if(payload == 220): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('z\n', 'utf-8'))
        if(payload == 230): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('L\n', 'utf-8'))
        if(payload == 240): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('U\n', 'utf-8'))
        if(payload == 250): 
            print("Valor nuevo:", payload)
            arduino.write(bytes('N\n', 'utf-8'))
                

    if(feed_id == feedPush1):
        if(payload == '0'):
            print('Push1: OFF')
            arduino.write(bytes('0\n', 'utf-8'))
        if(payload == '1'):
            print('Push1: ON')
            arduino.write(bytes('1\n', 'utf-8'))
    if(feed_id == feedPush2):
        if(payload == '0'):
            print('Push2: OFF')
            arduino.write(bytes('0\n', 'utf-8'))
        if(payload == '1'):
            print('Push2: ON')
            arduino.write(bytes('2\n', 'utf-8'))
    if(feed_id == feedPush3):
        if(payload == '0'):
            print('Push3: OFF')
            arduino.write(bytes('0\n', 'utf-8'))
        if(payload == '1'):
            print('Push3: ON')
            arduino.write(bytes('3\n', 'utf-8'))
    

        


    
    


try:
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

    # Setup the callback functions defined above.
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message

    # Connect to the Adafruit IO server.
    client.connect()
    client.loop_background()
              
    arduino = serial.Serial('COM6', baudrate =9600, timeout = 1)
    
    "Nano habla con Adafruit"
    while True:    
        mensaje = arduino.readline().decode('utf-8')
        if(mensaje == 'serv1\n'):
            print('serv1\n')
            client.publish(feedServ1, 1)
        if(mensaje == 'serv2\n'):
            print('serv2\n')
            client.publish(feedServ2, 2)
        if(mensaje == 'serv3\n'):
            print('serv3\n')
            client.publish(feedServ3, 3)
        if(mensaje == 'serv4\n'):
            print('serv4\n')
            client.publish(feedServ4, 4)
        time.sleep(3)
        
        
except KeyboardInterrupt:
    print("Salimos del programa")
    if arduino.is_open:
        arduino.close()
    sys.exit(1)