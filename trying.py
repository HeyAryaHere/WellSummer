import random
from tkinter import *
from tkinter.messagebox import showinfo

def main():
    
    def reply():
        showinfo(title="popup")
    from distutils import text_file
    def automatic():
        for x in range(21):
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            sing_list = ["+", "-"]
            text_file=open("txt.py","w")
            n = random.choice(sing_list)
            text_file.write(f"{x}{n}{y}")
            text_file.close()
    window = Tk()
    button = Button(window, text="Generate Automatically", command=main)
    button.pack()
    window.mainloop()

main()

'''
def by_number():
    print(input(str('What should be your first number?')))
'''
