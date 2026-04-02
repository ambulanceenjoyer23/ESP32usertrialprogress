# My Project
***
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
10. Atleast 11 jumper wires

## What the program does
- Pressing the button increments the counter and moves on the next state
- **State 0**: The program initially starts with all output devices switched off as counter is 0
- **State 1**: Switches on the red LED and trigeering a rainbow cycle using the RGB LED
- **State 2**: Switches on the blue LED and triggers a fire effect instead of the rainbow cycle using the RGB LED
- **State 3**: Switches on the green LED and sounds the buzzer
- To reset the cycle, press the button again

### Notes:
- The program uses blocking loops (sleep_ms) as i haven't used interrupts yet
- Future improvements will include interrupts or non-blocking logic for smoother operation
- To transition states, look out for the prompts that ask you to press the button and hold it for a second then release

## Circuit image
![Breadboard image](https://github.com/user-attachments/assets/b69afec7-691b-4448-a702-476aebc9c1c2)





