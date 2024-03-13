import paho.mqtt.client as mqtt
from flask_mqtt import Mqtt

a ="test.mosquitto.org"
b=1883
#n=int(input("enter no messages"))
r="hi"

def on_connect(client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    client.subscribe("test")
    
def on_message(client, userdata, msg):
    print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


mqtt_server = a
mqtt_port = b


client.connect(mqtt_server,mqtt_port,60);
client.loop_start()
for i in range(1):
    client.publish("test",r)
    
    print(str(client.subscribe("test")))
    print ("Message Sent")
    
client.loop_stop()

client.disconnect()



n=int(input("enter no. of messages"))
def on_message(client, userdata, msg):
   print(f"Received {msg.payload.decode()} from {msg.topic} topic")

client = mqtt.Client()
client.on_message = on_message
client.tls_set(
    ca_certs=r"C:\Users\Sujoy chatterjee\Downloads\mosquitto.org (1).crt",tls_version=mqtt.ssl.PROTOCOL_TLSv1_2)

client.connect("test.mosquitto.org",8883,60);
#client.loop_start()
for i in range(1):
    a=str(client.subscribe("test")))
    #socketio.emit('mqtt_message', data=data)
#client.loop_stop()
client.disconnect()
