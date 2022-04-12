from tkinter import *

window = Tk()
window.title("first gui")
window.minsize(width=500, height=300)

my_label = Label(text="label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)


def button_click():
    some = input.get()
    my_label["text"] = some


button = Button(text="click me", command=button_click)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=2, row=0)



window.mainloop()
