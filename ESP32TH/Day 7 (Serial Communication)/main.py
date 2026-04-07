from machine import UART
import time

print("ESP32 initialization complete!")
uart=UART(1, baudrate=115200, bits=8, parity=0, rx=5, tx=2, timeout=10)
uart.write("Hello PC")



while True:
    
#     val=time.ticks_us()
    uart.write(f"Running time: {time.ticks_ms()} s")
    uart.read()
#     time.sleep(1)
#     # Filter even numbers
#     print(f"{time.ticks_diff(time.ticks_us(),val)}")
#     time.sleep_ms(500)
#     print(f"Newer differnce: {time.ticks_diff(time.ticks_us(),val)}")

    
