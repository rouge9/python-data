from tkinter import *

window = Tk()
window.title("first gui")
window.minsize(width=500, height=300)

my_label = Label(text="label", font=("Arial", 24, "italic"))
my_label.pack()


def button_click():
    some = input.get()
    my_label["text"] = some


button = Button(text="click me", command=button_click)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()
