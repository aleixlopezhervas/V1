############  INSTALAR ##############
# paho-mqtt, version 1.6.1
#####################################

import paho.mqtt.client as mqtt
import json
from dronLink.Dron import Dron

# Usar STUDENT_ID fijo 'juan' según petición del usuario
STUDENT_ID = "juan2"
print(f"[AutopilotService] usando STUDENT_ID={STUDENT_ID}")

# variable global mínima para almacenar a qué tópico responder
sending_topic = None

# esta función sirve para publicar los eventos resultantes de las acciones solicitadas
def publish_event (event):
    global sending_topic, client
    if sending_topic:
        client.publish(sending_topic + '/'+event)
    else:
        client.publish(f'autopilotServiceDemo/{STUDENT_ID}/events/{event}')


def publish_telemetry_info (telemetry_info):
    # cuando reciba datos de telemetría los publico
    global sending_topic, client
    if sending_topic:
        client.publish(sending_topic + '/telemetryInfo', json.dumps(telemetry_info))
    else:
        client.publish(f'autopilotServiceDemo/{STUDENT_ID}/telemetryInfo', json.dumps(telemetry_info))


def on_message(cli, userdata, message):
    global  sending_topic, client
    global dron
    # el mensaje que se recibe tiene este formato:
    #    "origen"/autopilotServiceDemo/"command"
    # tengo que averiguar el origen y el command
    splited = message.topic.split("/")
    origin = splited[0] if len(splited)>0 else ''
    command = splited[2] if len(splited)>2 else ''

    sending_topic = "autopilotServiceDemo/" + origin

    if command == 'connect':
        connection_string = 'tcp:127.0.0.1:5763'
        baud = 115200
        dron.connect(connection_string, baud, freq=10)
        publish_event('connected')

    if command == 'arm_takeOff':
        if dron.state == 'connected':
            print ('vamos a armar')
            dron.arm()
            print ('vamos a despegar')
            dron.takeOff(5, blocking=False, callback=publish_event, params='flying')

    if command == 'go':
        if dron.state == 'flying':
            payload = message.payload.decode("utf-8")
            # aceptar formatos: "Direction" o "Direction|Speed"
            try:
                if '|' in payload:
                    parts = payload.split('|')
                    direction = parts[0]
                    try:
                        speed = float(parts[1])
                        # aplicar velocidad solicitada
                        try:
                            dron.changeNavSpeed(speed)
                        except Exception as e:
                            print('go: error aplicando changeNavSpeed:', e)
                    except Exception:
                        # si no es número, ignoramos speed
                        direction = payload
                else:
                    direction = payload
                # ejecutar navegación
                dron.go(direction)
            except Exception as e:
                print('Error procesando go payload:', payload, e)

    if command == 'changeHeading':
        try:
            payload = message.payload.decode("utf-8")
            if payload is None or payload == '':
                print('changeHeading: payload vacío')
            else:
                deg = float(payload) % 360
                if dron.state == 'flying':
                    try:
                        current = dron.heading
                        if current is None:
                            dron.changeHeading(deg, blocking=False)
                        else:
                            cur = float(current) % 360
                            delta = (deg - cur + 360) % 360
                            if delta > 180:
                                offset = 360 - delta
                                direction = 'ccw'
                            else:
                                offset = delta
                                direction = 'cw'
                            if offset < 1.0:
                                print(f'changeHeading: ya cerca de {deg}° (actual {cur}°), offset {offset}°')
                            else:
                                dron.rotate(offset, direction=direction, blocking=False)
                    except Exception as e:
                        print('Error intentando rotate, fallback a changeHeading:', e)
                        try:
                            dron.changeHeading(deg, blocking=False)
                        except Exception as e2:
                            print('Fallback changeHeading también falló:', e2)
                else:
                    print('changeHeading ignorado: dron no en estado flying')
        except Exception as e:
            print('Error procesando changeHeading:', e)

    if command == 'changeNavSpeed':
        try:
            payload = message.payload.decode('utf-8')
            if payload is None or payload == '':
                print('changeNavSpeed: payload vacío')
            else:
                try:
                    speed = float(payload)
                except Exception:
                    print('changeNavSpeed: payload no numérico:', payload)
                    speed = None
                if speed is not None:
                    try:
                        dron.changeNavSpeed(speed)
                    except Exception as e:
                        print('Error aplicando changeNavSpeed en dron:', e)
        except Exception as e:
            print('Error procesando changeNavSpeed:', e)

    if command == 'Land':
        if dron.state == 'flying':
            dron.Land(blocking=False, callback=publish_event, params='landed')

    if command == 'RTL':
        if dron.state == 'flying':
            dron.RTL(blocking=False, callback=publish_event, params='atHome')

    if command == 'startTelemetry':
        dron.send_telemetry_info(publish_telemetry_info)

    if command == 'stopTelemetry':
        dron.stop_sending_telemetry_info()


def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=",rc)
    else:
        print("Bad connection Returned code=",rc)


dron = Dron()

client = mqtt.Client(f"autopilotServiceDemo_{STUDENT_ID}", transport="websockets")

# me conecto al broker publico y gratuito
broker_address = "broker.hivemq.com"
broker_port = 8000

client.on_message = on_message
client.on_connect = on_connect
client.connect (broker_address,broker_port)

# me subscribo a todos los mensajes cuyo destino sea este servicio
client.subscribe(f"{STUDENT_ID}/autopilotServiceDemo/#")
print (f'AutopilotServiceDemo esperando peticiones en: {STUDENT_ID}/autopilotServiceDemo/#')
client.loop_forever()
