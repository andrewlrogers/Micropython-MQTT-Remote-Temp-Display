from time import sleep
import machine
from umqtt.simple import MQTTClient

##### VARIABLES ####

#MQTT variables
server = "10.0.1.2"
topic = "temp1"
client = "sensor1"

#Temp Variables
i2c = machine.I2C(machine.Pin(5), machine.Pin(4)) #initialize i2c
#i2c variables depend on device. Im using adafruit.com/product/1782
i2cDeviceAddress = 24
i2cRegisterAddress = 5
i2cNumBytesToRead = 2
data = bytearray(2)

# I have the built in LED on the Feather Huzzah set to blink when reading the temp
led0 = machine.Pin(0, machine.Pin.OUT)

#### FUNCTIONS ####
#This converts the data from the temp sensor into an integer.
#code is from learn.adafruit.com/micropython-hardware-i2c-devices
def convert_temp(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    temp = int(round(((temp * 9)/5)+32)) #converts the temp to F and makes it a nice round int for the display.
    return temp

#### Main Program ####
# Publish Temp.
def pub_temp():
    while True:
        led0.low() #Turns LED on
        sleep(.5)
        sensor_data = i2c.readfrom_mem(i2cDeviceAddress, i2cRegisterAddress, i2cNumBytesToRead) #read sensor
        sensor_temp = convert_temp(sensor_data) #creates a new variable made
        c.publish(topic, str(sensor_temp)) #publish data MQTT broker
        print(sensor_temp) #To monitor from the serial repl.
        led0.high() #Turns LED off
        sleep(1) #Sleep interval

sleep(5)
#connect to MQTT
c = MQTTClient(client, server)
c.connect()

pub_temp() #Calls the main program
c.disconnect() #Disconnects from server
