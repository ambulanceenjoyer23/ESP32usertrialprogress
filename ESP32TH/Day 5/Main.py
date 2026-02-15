import random
from machine import Pin,PWM
from time import sleep_ms
from Random_color_light import set_color, rainbow_cycle

pins=[15,2,4]

pwmRed=PWM(Pin(pins[0]),10000)
pwmGreen=PWM(Pin(pins[1]),10000)
pwmBlue=PWM(Pin(pins[2]),10000)
pwmList=[pwmRed,pwmGreen,pwmBlue]

set_color(*pwmList,0,0,0)
sleep_ms(500)

#pass PWM RGB List as 3 using *pwmList
rainbow_cycle(*pwmList)



