from machine import Pin
from time import sleep_ms

pins=[15,2,0,4,5,18,19,21,22,23]  #array of output GPIO's

#incrementally speed up by 25% each step after halfpoint LED lights up
def slowdown(i,sleep_value,length):
    if (i>4):
        sleep_value=sleep_value*i*0.25 
    elif(i<=4 or i==(length-1)): #reset sleep_value to 100 if loop ends or less than halfway
        sleep_value=100
    return sleep_value

def showled():
    length=len(pins)
    print (length)
    sleep_value=int(100)
    for i in range (0,length): #top to bottom loop on LED bar
        led=Pin(pins[i],Pin.OUT)
        sleep_value=int(slowdown(i,sleep_value,length)) #speed of next LED determined by function
        print(sleep_value) #debug purposes, please ignore as i know its annoying for other viewers and will change in future code
        led.value(1)
        sleep_ms(int(sleep_value))
        led.value(0)
    for i in range (0,length): #bottom to top loop
        led=Pin(pins[length-i-1],Pin.OUT)
        sleep_value=int(slowdown(i,sleep_value,length))
        print(sleep_value) #ignore
        led.value(1)
        sleep_ms(sleep_value)
        led.value(0)
        
while True:
    showled()
