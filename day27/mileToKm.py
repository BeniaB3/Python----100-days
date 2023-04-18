from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    return km


def change_label3():
    label3.config(text=miles_to_km())


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=100, pady=50)

entry = Entry(width=10)
entry.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=change_label3)
button.grid(column=1, row=2)

window.mainloop()
