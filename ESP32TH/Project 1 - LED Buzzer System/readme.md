# My Project
***
This project is a button-controlled system built on the ESP32-Wrover that cycles through four different operating states.

## Components used
***
1. Red LED
2. Blue LED
3. Green LED
4. Common anode RGB LED
5. Passive buzzer
6. Button
7. NPN BJT transistor (S8060)
8. 220Ω resistor - 6x, for LED's
9. 1KΩ resistor - 2x
10. Atleast 11 jumper wires

## What the program does
***
- The program initially starts with all output devices switched off as counter is 0
- Pressing the button once increments the counter, thus moving to state 1, switching on the red LED and trigeering a rainbow cycle using the RGB LED
- Pressing the button again moves to state 2, Switching on the blue LED and triggers a fire effect instead of the rainbow cycle using the RGB LED
- A final press keeps moves to state 3, which is similar to state 3, Switching on the green LED and sounding the buzzer
- To reset the cycle, press the button again

### Notes:
- The program uses blocking loops as i haven't used interrupts yet, which will be used in fututre projects
- To transition states, look out for the prompts that ask you to press the button and hold it for a second then release
- 


