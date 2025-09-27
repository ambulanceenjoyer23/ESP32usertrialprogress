from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT)

while True: #check if input is integer and convert to int
    x=input("Please enter number of times to loop: ")
    if x.isdigit():
        x_int=int(x)
        break
        
    else:
        print("Enter an integer")
        
print(type(x))
print(type(x_int))
        


for t in range(x_int):   #flash LED with user input
    led.value(0)
    sleep_ms(300)
    led.value(1)
    sleep_ms(300)
    

        
        
        
    
