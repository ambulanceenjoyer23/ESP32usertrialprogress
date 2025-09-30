from machine import Pin
from time import sleep_ms

#traffic lights colours and button
red=Pin(2,Pin.OUT)
yellow_or_blue=Pin(14,Pin.OUT)
green=Pin(33,Pin.OUT)
button=Pin(13,Pin.IN,Pin.PULL_UP)  #Input button

def blink_yelloworblue(): #blink yellow for a second
    for x in range(5):
        yellow_or_blue.value(1)
        sleep_ms(100)
        yellow_or_blue.value(0)
        sleep_ms(100)
        
#inverts led value
def reverse_gpio(pin):  #save as module for use in other files
    if pin.value():  #
        pin.value(0)
    else:
         pin.value(1)
         
red.value(1)


try:
    while True:
        red.value(1)  #default to red when not pressed
        yellow_or_blue.value(0)
        green.value(0)
        while not button.value(): #Make traffic light green
            sleep_ms(20)
            reverse_gpio(red) #turn off red
            sleep_ms(20)
            reverse_gpio(green) #turn on green for 3 sec
            sleep_ms(3000)
            reverse_gpio(green)  #turn off green
            blink_yelloworblue()  #warn drivers with blinking yellow/blue LED for 1 sec
            #will anger drivers but just for testing purposes
            while not button.value():
                sleep_ms(20) #debounce
                      
except:
    pass
            

