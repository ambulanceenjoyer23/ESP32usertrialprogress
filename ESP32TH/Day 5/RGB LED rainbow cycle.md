RGB LED Rainbow Cycle (Messy But Working Version)

This is my attempt at a rainbow cycle for RGB LEDs using MicroPython.
I mostly figured out the logic myself, needed a little help for the last segment (Blue → Red), but overall it’s running and looks pretty cool. 

What it does:
-Smoothly fades colors between Red → Green → Blue → Red
-Uses common-anode / active-low LEDs (0 = full brightness, 1023 = off)
-Works with ESP32 / ESP8266 or any board with PWM capable pins

Hardware:
RGB LED (common-anode)
ESP32 / ESP8266 (or similar)
3 PWM pins connected to Red, Green, Blue pins
Pins in my example code: GPIO: [15, 2, 4]  # Red, Green, Blue

How it works:
Each color fades in/out in steps of 0–1023 PWM
Red → Yellow -> Green → Cyan -> Blue → Magenta -> Red cycle
Uses set_color() function with active-low logic:

def set_color(red, green, blue, rValue, gValue, bValue):
    red.duty(1023 - rValue)
    green.duty(1023 - gValue)
    blue.duty(1023 - bValue)

0 = full brightness, 1023 = off
Helps create smooth gradient transitions


How to use:
Connect your RGB LED to PWM pins (common-anode).
Copy set_color() and rainbow_cycle() into your main MicroPython script.
Call rainbow_cycle(redPWM, greenPWM, bluePWM).

Notes:
sleep_ms() controls speed — lower = faster transitions, higher = slower
Keep duty values 0–1023 to avoid errors
The prints in the code show RGB values per step (helped me debug)
Optional video title if you post it:

Video:
https://github.com/user-attachments/assets/df96fffe-0fc2-40df-a637-4841e4e58746




