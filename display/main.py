import machine, ht16k33_seg, time
from umqtt.simple import MQTTClient
import urequests, json


#MQTT variables
server="10.0.1.2"
topic = "temp1"
client = "display_dash"
c = MQTTClient(client, server)
c.connect()

#display variables
i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
display = ht16k33_seg.Seg7x4(i2c)
display.fill(0) #clears the display
display.show()
display.brightness(0) #sets display to minimum brightness


# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print(msg)
    msg = round(int(msg)) #converts byte to int for display
    display.number(msg) #writes message to display
    display.show()

def main():
    while True:
        c.set_callback(sub_cb)
        c.subscribe(topic)
        display.fill(0) #clears the display
        display.show()
        c.check_msg()
        time.sleep(1)

time.sleep(2)
main()
