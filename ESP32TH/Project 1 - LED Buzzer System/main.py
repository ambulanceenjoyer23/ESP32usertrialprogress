from machine import Pin,PWM
from time import sleep_ms
from math import radians,sin
from RGB_LED_module import RGBLED
from Button_module import Button

#Output
rainbowLEDPins=[15,2,0] #Rainbow LED pins - Can be set to whatever pin you want
#IndiviusaLED's to indiciate # of presses (1 to 3)
rLED=Pin(14,Pin.OUT)
bLED=Pin(12,Pin.OUT)
gLED=Pin(13,Pin.OUT)
passiveBuzzer=PWM(Pin(27))
rainbowLED=RGBLED(*rainbowLEDPins) #Common anode Rgb LED (Can produce any colour)

#Input
controlButton=Button(4,20)

def state_1(): #Trigger rainbow effect
    rLED.value(1)
    bLED.value(0)
    gLED.value(0)
    rainbowLED.rainbow_cycle()
    
def state_2(): #Trigger fire effect
    rLED.value(1)
    bLED.value(1)
    gLED.value(0)
    rainbowLED.fire_effect()

def sound_alarm():
    frequency=2000
    passiveBuzzer.init()
    #Varying pitch by using a Sin wave
    for x in range(0,360,1):
        y=radians(x)
        sinWave=sin(y)
        position=1000*sinWave
        wave=int(frequency+position)
        passiveBuzzer.freq(wave)
        passiveBuzzer.duty(256)
        sleep_ms(10)
        
def state_3(): #Flash all the lights and sound alarm
    rLED.value(1)
    bLED.value(1)
    gLED.value(1)
    rainbowLED.fire_effect()
    sound_alarm()

counter=0    
pressed=False
passiveBuzzer.deinit()

while True:
    
    #Handles button presses, Blocked by loops
    if controlButton.press_action():
        pressed=True
        if pressed:
            counter+=1
            pressed=not pressed
            
    if counter==0: #Everything switched off
        rLED.value(0)
        bLED.value(0)
        gLED.value(0)
        rainbowLED.set_color(0,0,0)
        print("Press the button now to transition to rainbow effect")
    elif counter==1: #Red LED on & Rainbow LED effect 
        state_1()
        #Blocking behaviour
        print("Press the button now to transition to fire effect")
        sleep_ms(1200)
    elif counter==2: #Red, Blue, Green LED on & fire LED effect
        state_2()
        #Blocking behaviour
        print("Press the button now to go to into alarm mode")
        sleep_ms(1200)
    elif counter==3: # Everything switched on & trigger alarm
        passiveBuzzer.init()
        state_3()
        #Blocking behaviour
        print("Press the button now to switch off everything and repeat loop")
        sleep_ms(1200)
    else:
        #reset loop
        counter=0
        passiveBuzzer.deinit()
    
    print(counter)
    sleep_ms(200)

        
#     if controlButton.press_action():
#         rLED.value(1)
#         gLED.value(0)
#         gLED.value(1)
#         
#         rainbowLED.set_color(50,500,750)
    
