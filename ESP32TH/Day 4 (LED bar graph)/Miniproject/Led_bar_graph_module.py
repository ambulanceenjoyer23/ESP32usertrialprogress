from machine import PWM, Pin
from time import sleep_ms

class BarGraphPWM():
    ledBarPin=[21,19,18,5,4,0,2,15] #for incrementing range purposes only

    #constructor for 8 LED bar graph
    def __init__ (self, pwmLed0:int=21, pwmLed1:int=19, pwmLed2:int=18,pwmLed3:int=5, pwmLed4:int=4, pwmLed5:int=0,pwmLed6:int=2,pwmLed7:int=15):
        self._pwmLed0=PWM(Pin(pwmLed0),10000)
        self._pwmLed1=PWM(Pin(pwmLed1),10000)
        self._pwmLed2=PWM(Pin(pwmLed2),10000)
        self._pwmLed3=PWM(Pin(pwmLed3),10000)
        self._pwmLed4=PWM(Pin(pwmLed4),10000)
        self._pwmLed5=PWM(Pin(pwmLed5),10000)
        self._pwmLed6=PWM(Pin(pwmLed6),10000)
        self._pwmLed7=PWM(Pin(pwmLed7),10000)
        
    #change duty cycle of corresponding indiviusal LED
    def led_write(self, led:int, value:int):
        pwm=getattr(self,f"_pwmLed{led}",None)
        print (pwm)
        if pwm is None:
            print ("invalid pwmchannel")
            return
        pwm.duty(value)
        sleep_ms(50)
        
    #deconstructor
    def deinit(self):
            self._pwmLed0.deinit()
            self._pwmLed1.deinit()
            self._pwmLed2.deinit()
            self._pwmLed3.deinit()
            self._pwmLed4.deinit()
            self._pwmLed5.deinit()
            self._pwmLed6.deinit()
            self._pwmLed7.deinit()



        

