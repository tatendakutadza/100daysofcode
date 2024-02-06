# Simple calculator
# Main concepts: Tkinter

from tkinter import *

def click(text):
    if text == 1:
        return 1

window = Tk()
window.title("Calculator")

entry = Entry(window)
entry.grid(row=0, column=0, sticky=W, pady=2, columnspan=4)
btn_1 = Button(window, text="   1   ", command=click)
btn_1.grid(row=1, column=0, sticky=W, pady=2)
btn_2 = Button(window, text="   2   ", command=click)
btn_2.grid(row=1, column=1, sticky=W, pady=2)
btn_3 = Button(window, text="   3   ", command=click)
btn_3.grid(row=1, column=2, sticky=W, pady=2)
btn_4 = Button(window, text="   4   ", command=click)
btn_4.grid(row=2, column=0, sticky=W, pady=2)
btn_5 = Button(window, text="   5   ", command=click)
btn_5.grid(row=2, column=1, sticky=W, pady=2)
btn_6 = Button(window, text="   6   ", command=click)
btn_6.grid(row=2, column=2, sticky=W, pady=2)
btn_7 = Button(window, text="   7   ", command=click)
btn_7.grid(row=3, column=0, sticky=W, pady=2)
btn_8 = Button(window, text="   8   ", command=click)
btn_8.grid(row=3, column=1, sticky=W, pady=2)
btn_9 = Button(window, text="   9   ", command=click)
btn_9.grid(row=3, column=2, sticky=W, pady=2)
btn_0=Button(window, text="   0   ", command=click)
btn_0.grid(row=4, column=1, sticky=W, pady=2)
btn_cancel=Button(window, text="delete ", command=click)
btn_cancel.grid(row=4, column=0, sticky=W, pady=2)
btn_calculate=Button(window, text="   =   ", command=click)
btn_calculate.grid(row=4, column=2, sticky=W, pady=2)
btn_add=Button(window, text="   +   ", command=click)
btn_add.grid(row=1, column=3, sticky=W, pady=2)
btn_subtract=Button(window, text="   -   ", command=click)
btn_subtract.grid(row=2, column=3, sticky=W, pady=2)
btn_divide=Button(window, text="   /   ", command=click)
btn_divide.grid(row=3, column=3, sticky=W, pady=2)
btn_multiply=Button(window, text="   x   ", command=click)
btn_multiply.grid(row=4, column=3, sticky=W, pady=2)
window.mainloop()
