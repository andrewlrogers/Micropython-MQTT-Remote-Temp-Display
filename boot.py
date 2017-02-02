# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SSID', 'PASSWORD') #change to your SSID and PASSWORD
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

#connect to local network
do_connect()
gc.collect()
