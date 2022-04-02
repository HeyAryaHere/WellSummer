import random
from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title="popup")


def automatic():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    sing_list = ["+", "-"]

    if x > y:
        print(f"{x}+{y}")
    else:
        n = random.choice(sing_list)
        print(f"{x}{n}{y}")


window = Tk()
button = Button(window, text="Generate Automatically", command=automatic)
button.pack()
window.mainloop()
