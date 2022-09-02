from tkinter import *
import random

window = Tk()
window.minsize(600,600)
window.maxsize(600,600)
window.title('Roll the Dice')

label = Label(window,font=('bold',400))
def roll():
    number = ['\u2680','\u2681','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()

heading = Label(window,text='Roll the Dice',font=('bold',50),bg='grey')
heading.pack(fill=X)

button = Button(window,text='Roll',font=('normal',25),command=lambda:roll())
button.pack()
window.mainloop()