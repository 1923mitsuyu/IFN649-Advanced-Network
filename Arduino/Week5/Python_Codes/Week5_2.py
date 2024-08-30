# Publish Topic on Rasberry pi to EC2 instance
import paho.mqtt.publish as publish

# Send a message "Hello World" to topic ifn649
publish.single("ifn649", "Hello World", hostname="ip-addres")
print("Done")
