# My Project
This project is a button-controlled system built on the ESP32-Wrover that cycles through four different operating states.

## Components used
1. Red LED
2. Blue LED
3. Green LED
4. [Common anode RGB LED](https://www.sparkfun.com/led-rgb-clear-common-anode.html)
5. Passive buzzer 
6. Button
7. [NPN BJT transistor](https://www.google.com/imgres?q=npn%20transistor%20s8050&imgurl=https%3A%2F%2Fwww.rawlix.com%2FDataImages%2FProducts%2F637267027679472833_0large.webp&imgrefurl=https%3A%2F%2Fwww.rawlix.com%2Fproduct%2Fnpn-transistor-s8050-637250186907564246%3Fsrsltid%3DAfmBOor1Bgph68aSwhFac38cHiGsw8Li3BQwt4NCFBTxIiWjcfrc5Yfo&docid=pkc0Pk0KFULLMM&tbnid=Kc0abhzMdeZbiM&vet=12ahUKEwjW7O_KqtCTAxUw8QIHHV-VMRIQnPAOegQIGxAB..i&w=566&h=519&hcb=2&ved=2ahUKEwjW7O_KqtCTAxUw8QIHHV-VMRIQnPAOegQIGxAB) (S8060) (for Buzzer as it is a 5V device)
8. 220Ω resistor - 6x (3x for red, green, blue LED's & 3x for RGB common anode LED)
9. 1KΩ resistor - 1x (1tx for BJT base, 1x optional for reducing buzzer noise)
10. At least 11 jumper wires

## What the program does
- Pressing the button increments the counter and moves on the next state
- **State 0**: The program initially starts with all output devices switched off as counter is 0
- **State 1**: Switches on the red LED and trigerring a rainbow cycle using the RGB LED
- **State 2**: Switches on the blue LED and triggers a fire effect instead of the rainbow cycle using the RGB LED
- **State 3**: Switches on the green LED and sounds the buzzer
- To reset the cycle, press the button again

### Notes:
- The program uses blocking loops (sleep_ms) as i haven't used interrupts yet
- Future improvements will include interrupts or non-blocking logic for smoother operation
- To transition states, look out for the prompts that ask you to press the button and hold it for a second then release

## Demo
[Watch the video here](https://drive.google.com/file/d/11MEM2zqU6sXwgv0sDUn7MeOmi4zYhrB3/view?usp=sharing)

## Circuit image
![Breadboard image](https://github.com/user-attachments/assets/b69afec7-691b-4448-a702-476aebc9c1c2)

## File structure
- Main.py

**Modules**
- Button_module.py
- RGB_LED_module.py


## Wiring
### BJT and buzzer
GPIO27 -> 1kΩ -> BJT Base
5V rail -> 1kΩ resistor(optional) -> Passive Buzzer -> BJT Collector
Ground -> BJT Emitter

### RGB LED (Common Anode)
- 3.3V -> Common anode
- R (GPIO15) -> 220Ω -> R pin
- G (GPIO2)  -> 220Ω -> G pin
- B (GPIO0)  -> 220Ω -> B pin

### Single-color LEDs:
- Red LED: GPIO14 -> 220Ω -> Anode -> Cathode -> GND
- Green LED: GPIO13 -> 220Ω -> Anode -> Cathode -> GND
- Blue LED: GPIO12 -> 220Ω -> Anode -> Cathode -> GND

### Button (with internal pull-up):
GPIO4 --- Button --- GND

### Notes:
- All resistors are current-limiting or base-limiting.
- RGB LED is common-anode, so connect to 3.3V and the other pins to corresponding GPIO pins as they act as current sinks/ground
- Buzzer uses transistor as a switch as it a 5V device; GPIO27 drives the transistor base.
- Please use the ESP32 internal pull up configuration as an external resistor is not used here to pull up
    `
  self.button=Pin(pin,Pin.IN,Pin.PULL_UP)
  `






