from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    my_text = input.get()
    my_label.config(text=my_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry


input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# import turtle
#
# tim = turtle.Turtle()
# tim.write("Some text", font=("Arial", 24, "normal"))
#
window.mainloop()
