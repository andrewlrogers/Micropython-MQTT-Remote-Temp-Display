# Micropython-MQTT-Remote-Temp-Display

# About
[In response to this thread](http://forum.micropython.org/viewtopic.php?t=2895). This code successfully reads data from a temperature sensor and sends it via MQTT to a separate display.  

# Like this

`Temp Sensor Feather ---[publish to topic1]---> RaspberryPi MQTT broker ---[subscribe to topic1]---> Display Feather`

# Items Used
* [2x Adafruit Feather HUZZAH with ESP8266 WiFi](https://www.adafruit.com/product/2821)
* [1x Adafruit 4-Digit 7-Segment LED Matrix Display FeatherWing](https://www.adafruit.com/products/3088)
* [1x MCP9808 High Accuracy I2C Temperature Sensor Breakout Board](https://www.adafruit.com/products/1782)
* [1x Raspberry Pi running Mosquitto](http://www.switchdoc.com/2016/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/)
* Assorted cables, wires, soldering iron, solder, and tools

# More Information

* [Setting up Mosquitto on a Raspberry Pi](http://www.switchdoc.com/2016/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/)
* [Micropython Basics on Adafruit](https://learn.adafruit.com/micropython-basics-what-is-micropython)
* [Actually, all the Micropython tutorials on Adafruit](https://learn.adafruit.com/category/micropython)
* [This guy's post on the Adafruit Forum](https://forums.adafruit.com/viewtopic.php?t=104870)
