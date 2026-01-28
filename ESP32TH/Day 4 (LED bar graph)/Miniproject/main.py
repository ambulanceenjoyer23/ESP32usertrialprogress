from Led_bar_graph_module import BarGraphPWM
from machine import Pin,PWM
from time import sleep_ms

ledBarPin=[21,19,18,5,4,0,2,15]
tailLength=len(ledBarPin)  #8 Leds
maxBrightness=1023     #brightest LED intensity
ledBarGraph=BarGraphPWM(*ledBarPin)  #pass list as 8  numbers

ledBarGraph:BarGraphPWM
varyingLedIntensities=[int(maxBrightness/(2**x)) for x in range(tailLength)]
print (varyingLedIntensities)

#Turn off LEDs in LED bar graph 
for x in range(tailLength):
    ledBarGraph.led_write(x,0)
    #this works by writing to a certian chainnel and what duty cycle to use (100%,87.5%,75% etcc)
sleep_ms(4000)

#flow light
while True:
    for x in range(tailLength):  #flow light from top to bottom (0 to 7)
        ledBarGraph.led_write(x,varyingLedIntensities[0]) #Brightest from list at index 0
        for y in range(x):
            temp=x-y
            ledBarGraph.led_write(y,varyingLedIntensities[temp])
        sleep_ms(50)
    for x in reversed(range(tailLength)): #reverse flow from 7 to 0
        ledBarGraph.led_write(x,varyingLedIntensities[0])
        for y in range(x+1, tailLength):
            temp=y-x
            ledBarGraph.led_write(y,varyingLedIntensities[temp])
        sleep_ms(50)

        
        
        
            
                
                
            
        
        
    





