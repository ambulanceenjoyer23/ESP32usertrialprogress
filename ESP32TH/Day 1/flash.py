from time import sleep_ms
from machine import Pin

blue_light=Pin(2,Pin.OUT)
try:
    
    for i in range (0,1000):
        blue_light(1)
        sleep_ms(500)
        blue_light(0)
        sleep_ms(500)
        print("hello")
    
        
except:
    pass
    
        
    
