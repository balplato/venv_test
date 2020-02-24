import pyautogui as p
import getpass
import time
import bs4

bs4.BeautifulSoup


time.sleep(3)
#password = getpass.getpass(prompt="PROMPT: ")  # works only from cmd/terminal

#print(password)
# presses space-key 10 times once a second
p.press("space", presses=10, interval=1.0)

# then presses backspace 10 times once half a second
p.press("backspace", presses=10, interval=0.5)
