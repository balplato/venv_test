import pyautogui as p
import time

width = p.size()[0]
heigth = p.size()[1]

p.moveTo(10, heigth-10, 1)
time.sleep(1)
p.click()
p.moveTo(width/2, heigth/2, 0.5)
# waits 1 second
time.sleep(1)

p.write("sublime")
time.sleep(2)
p.press("tab")
p.press("enter")
time.sleep(2)
p.press("enter")
p.write("I've done it!", interval=0.1)
p.moveTo(width-10, 10, 1)
p.click()
p.moveTo(width/2, heigth/2, 1)