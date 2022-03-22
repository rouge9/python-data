from tkinter import *

window = Tk()
window.title("convertor")
window.config(padx=20, pady=20)


def calculate():
    mile = int(input.get())
    kilo = round(mile * 1.609)
    label_0["text"] = kilo


label_mile = Label(text="mile")
label_mile.grid(row=0, column=3)
label_is = Label(text="is equal to")
label_is.grid(row=1, column=0)
label_0 = Label(text="0")
label_0.grid(row=1, column=1)
label_km = Label(text="km")
label_km.grid(row=1, column=2)
input = Entry(textvariable="0")
input.grid(column=1, row=0)
button = Button(text="calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
