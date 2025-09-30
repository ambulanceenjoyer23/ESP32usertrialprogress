from machine import Pin
from time import sleep_ms
print("hello")

led=Pin(2,Pin.OUT)
button=Pin(13,Pin.IN,Pin.PULL_UP)



try:
    while True:
        print (button.value)
        if not button.value():
            led.value(1)
        else:
            led.value(0)
            
except:
    pass