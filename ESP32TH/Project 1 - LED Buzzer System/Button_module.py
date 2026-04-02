from machine import Pin
from time import sleep_ms

class Button:
    
    def __init__(self, pin:Pin, debounce:int):  #User sets Pin and desired debounce time
        self.button=Pin(pin,Pin.IN,Pin.PULL_UP)
        self.debounceTime=debounce
        
    def is_held(self,action=None): #To detect Holds & not presses
        if not self.button.value():
            sleep_ms(self.debounceTime)
            if action:
                action(self.debounceTime)
            return True
        else:
            return False
        
            
    def press_action(self, action=None): # Use button as switch, pass output functions in action argument if needed or leave blank
        if not self.button.value():  # Button is pressed (pull-up mode, 0 is pressed)
            sleep_ms(self.debounceTime)  # Debounce delay
            if not self.button.value():  # Confirm press
                if action:
                    action()  # Execute the action passed if argument passed(e.g., reverse GPIO)
                print("Button Pressed")  # Indicate press
                # Wait until the button is released
                while not self.button.value():  # Wait for release
                    sleep_ms(self.debounceTime)
                return True  
        return False  #return whether press or not for if conditions in main
            
        
    

