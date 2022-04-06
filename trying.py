import random
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from distutils import text_file

class main():

    def abc():
        window = Tk()

        def automatic():
                text_file= open('output.txt','w')

                for i in range(10):

                    x = random.randint(1, 9)
                    y = random.randint(0, 9)
                    sing_list = ["+", "-"]
                    
                    if x  < y:
                        text_file.write(f"\n{x}+{y}")
                    else:
                        s = random.choice(sing_list)
                        text_file.write(f"{x}{s}{y}\n.")

                text_file= open('output.txt','w')
            
        button = Button(window, text="Generate Automatically", command=automatic)
        button.pack()
        window.mainloop()

    abc()

main()
