from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    return km


def change_label3():
    zero_label.config(text=miles_to_km())


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=100, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

zero_label = Label(text="0")
zero_label.grid(column=1, row=1)


km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calcul_button = Button(text="Calculate", command=change_label3)
calcul_button.grid(column=1, row=2)

window.mainloop()
