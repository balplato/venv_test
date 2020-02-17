import pyautogui as p
import time

# waits 3 seconds
time.sleep(3)

# presses space-key 10 times once a second
p.press("space", presses=10, interval=1.0)

# then presses backspace 10 times once half a second
p.press("backspace", presses=10, interval=0.5)
