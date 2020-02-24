import random as r
from tkinter import *

def colorchanger():
    window.configure(bg='#CC0000')
def colorchanger2():
    window.configure(bg='#002020')
window = Tk()
window.title("Title")
window.geometry('700x700')
window.configure(bg='#002020')
mybutton = Button(width= 10, height= 10, command=colorchanger)

notmybutton = Button(width= 10, height= 10, command=colorchanger2)


mybutton.pack()
notmybutton.pack()

# run
window.mainloop()

print(r.randint(1, 10))

