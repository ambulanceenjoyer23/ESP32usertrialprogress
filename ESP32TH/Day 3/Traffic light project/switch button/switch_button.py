from machine import Pin
from time import sleep_ms
print("hello")

led=Pin(2,Pin.OUT) #red led
button=Pin(13,Pin.IN,Pin.PULL_UP)  #Input button

#inverts led value
def reverse_gpio(pin):  #save as module for use in other files
    if pin.value():  #
        pin.value(0)
    else:
         pin.value(1)
        


try:
    while True:
        if not button.value():              # Button pressed (active-low)
            sleep_ms(20)                    # Debounce delay
            if not button.value():          # Still pressed after debounce
                reverse_gpio(led)              # Toggle LED
                while not button.value():   # Wait for release
                    sleep_ms(20)            # Optional: shorter sleep
except:
    pass

