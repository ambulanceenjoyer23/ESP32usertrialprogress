# ESP32 LED Bar Graph Flowing Light

This is a simple project to make 8 LEDs on a bar graph **flow like a moving light** using PWM on an ESP32.  

It goes up (LED 0 → LED 7) and then down (LED 7 → LED 0) with a “tail” effect where LEDs behind the head get dimmer.

---

## What you need

- ESP32 dev board  
- 8 LEDs with resistors (~220Ω)  
- Jumper wires and breadboard  

---

## How to use

1. Copy `led_bar_graph_module.py` and `main.py` to your ESP32.  
2. Make sure the pins in `ledBarPin` match your wiring:

```python
ledBarPin = [21, 19, 18, 5, 4, 0, 2, 15]

Video:
https://drive.google.com/file/d/16xr1giLpapDAuAEaqUfuhhhhLtlrot2v/view?usp=sharing

Readme is AI generated but code is not, Used it for readme to make the project description easier to understand
