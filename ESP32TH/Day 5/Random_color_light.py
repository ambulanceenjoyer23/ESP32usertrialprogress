from machine import Pin,PWM
from time import sleep_ms
from random import randint

#1023 is 

def set_color(red:PWM,green:PWM,blue:PWM,rValue,gValue,bValue):
    #active low logic
    #Example:
    #red.duty(0) is bright red because RGB led GPIO pin is current sink that activate when Low
    #red.duty(1023) is very dim red or off because the anode is 3.3v and so is the red led GPIO so no current flows.
    red.duty(1023-rValue)
    green.duty(1023-gValue)
    blue.duty(1023-bValue)

#Red=0, green=85, blue=170, red=255, transition smoothly between tehm
def rainbow_cycle(red:PWM,green:PWM,blue:PWM):
    print ("initiating")
    tempPosition=0
    global redValue
    global greenValue
    global blueValue
    for i in range(256):
        if i<86:
            greenValue=int(i*(1023/85))  #Bright red at beggining and dims down slowly to no red
            redValue=int((85-i)*(1023/85))   #No green in beggining and slowly fades into bright green
            print(f"{redValue} + {greenValue}")
            set_color(red,green,blue,redValue,greenValue,0)
            sleep_ms(20)
        elif i<171:
            i2=i-85
            blueValue=int(i2*(1023/85))    #transition from bright green to bright blue smoothly
            greenValue=int((85-i2)*(1023/85))
            print(f"{greenValue}+ {blueValue}")
            set_color(red,green,blue,0,greenValue,blueValue)
            sleep_ms(20)
        else:
            i3=i-170
            print("i3 is "+str(i3))
            blueValue = (85 - i3) * 1023 // 85  #transition from bight blue to bright red smoothly
            redValue  = i3 * 1023 // 85
            print(f"{blueValue}+ {redValue}")
            set_color(red,green,blue,redValue,0,blueValue)
            sleep_ms(20)
            
        

        



    

