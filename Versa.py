from tkinter import *
import time

totalclicks = 0

autoclicker_enabled = False


def click():
    global totalclicks
    totalclicks += 1
    label.config(text=f"{totalclicks}")
    finishgame()

def clickx2():
    global totalclicks
    totalclicks += 2
    label.config(text=f"{totalclicks}")
    finishgame()

def clickx4():
    global totalclicks
    totalclicks += 8
    label.config(text=f"{totalclicks}")
    finishgame()

def autoclicker():
    global totalclicks, autoclicker_enabled
    if autoclicker_enabled:
        totalclicks += 1
        label.config(text=f"{totalclicks}")
        finishgame()
        window.after(100, autoclicker)

def getx2clicks():
    global totalclicks
    if totalclicks >= 100:
        totalclicks -= 100
        button.config(command=clickx2)
        buttonx2.config(command=getx4clicks, text="Click Me To Get X4 Clicks!(300)")
        label.config(text=f"{totalclicks}")
    else:
        print("not enough money")
def getx4clicks():
    global totalclicks
    if totalclicks >= 300:
        totalclicks -= 300
        button.config(command=clickx4)
        buttonx2.config(state=DISABLED,text="",font=("Arial",1))
        label.config(text=f"{totalclicks}")
        finishgame()
    else:
        print("not enough money")
def getautoclicker():
    global totalclicks, autoclicker_enabled
    if totalclicks >= 1000:
        totalclicks -= 1000
        autoclicker_enabled = True
        label.config(text=f"{totalclicks}")
        buttonauto.config(state=DISABLED, text=" ", font=("Arial", 0))
        autoclicker()

def finishgame():
    global totalclicks, autoclicker_enabled
    if totalclicks >= 5000:
            label.config(text="Thank You For Playing!")
            button.config(fg="black")
            button.config(font=("Arial",30))
            button.config(state=DISABLED)
            buttonx2.config(state=DISABLED, text="", font=("Arial", 50))
            buttonauto.config(state=DISABLED, text=" ", font=("Arial",0))
            autoclicker_enabled = False

window = Tk()
window.geometry("1200x1000")
window.title("Clicker Simulator")

button = Button(window,text="Click Me!")
button.config(font=("Arial",50,"bold"))
button.config(command=click)
button.place(relx=0.5, y=70, anchor='n')

buttonx2 = Button(window,text="Click Me To Get X2 Clicks!(100)")
buttonx2.config(font=("Arial",50,))
buttonx2.config(command=getx2clicks)
buttonx2.place(relx=0.5, y=150, anchor='n')

buttonauto = Button(window,text="Click Me To Get A AutoClicker(1000)")
buttonauto.config(font=("Arial",50,))
buttonauto.config(command=getautoclicker)
buttonauto.place(relx=0.5, y=230, anchor='n')

label = Label(window,
              text=f"{totalclicks}",
              font=("Arial",40,"bold"),
              )
label.place(relx=0.5, y=10, anchor='n')

window.mainloop()
