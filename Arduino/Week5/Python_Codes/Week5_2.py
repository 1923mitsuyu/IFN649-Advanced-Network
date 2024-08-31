# Publish Topic on Rasberry pi to EC2 instance
import paho.mqtt.publish as publish

# Send a message "LED_ON" to topic ifn649
publish.single("ifn649", "LED_ON", hostname="ip-addres")
print("Done")
