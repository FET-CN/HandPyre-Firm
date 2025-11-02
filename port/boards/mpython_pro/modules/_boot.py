import time
import gc
import uos
from flashbdev import bdev
from neopixel import NeoPixel
import ubinascii
import machine
from machine import Pin

Pin(12, Pin.OUT, value=0)

print("HRE: boot...")

try:
    if bdev:
        uos.mount(bdev, "/")
except OSError:
    import inisetup
    vfs = inisetup.setup()

print("    __  ______  ______")
print("   / / / / __ \\/ ____/")
print("  / /_/ / /_/ / __/   ")
print(" / __  / _, _/ /___   ")
print("/_/ /_/_/ |_/_____/   ")
print("                      ")
print("Fire at Command, Reborn in Hand")
print("")

for i in range(3):
    print("=$%#=")

print("")

# mac地址
# mac地址
mac = '$#mac:{}#$'.format(ubinascii.hexlify(machine.unique_id()).decode().upper())
print(mac)

print("")

# 上电后立即关闭rgb,防止随机灯亮问题
_rgb = NeoPixel(Pin(8, Pin.OUT), 4, 3, 1,0.1)
_rgb.write()
del _rgb

import lcd
lcd.draw_logo()

gc.collect()
