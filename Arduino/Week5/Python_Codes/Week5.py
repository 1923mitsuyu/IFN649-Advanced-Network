# Subscribe Topic (受信) on Rasberry pi
import paho.mqtt.client as mqtt
import serial 
import time 
import string

# Called when the connection with MQTT broker was successful 
def on_connect(client, userdata, flags, rc): 
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    # Subscribe to the topic ifn649
    client.subscribe("ifn649")

# Recieve the message on Raspberry pi from EC2 instance 
# Called when a message was delivered from topic ifn649
def on_message(client, userdata, msg): 
    print(msg.topic+" "+str(msg.payload))
    # Add a code to send this recieved message from EC2 to Ardino over Bluetooth
    ser = serial.Serial("/dev/rfcomm0", 9600) 
    ser.write(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("ip-addres", 1883, 60) 
client.loop_forever()



