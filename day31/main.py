import pandas
import pandas as pd
from tkinter import PhotoImage, Button
import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
fr_Words = []
current_card = {}
to_learn = {}

try:
    with open("data/words_to_learn.csv", "r") as f:
        if f.read().strip() == "":
            raise FileNotFoundError
        else:
            data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



name = data.columns[0]
for index, row in data.iterrows():
    fr_Words.append({"French": row[0], "English": row[1]})


def next_Card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(fr_Words) > 0:
        current_card = random.choice(fr_Words)
        canvas.itemconfig(word, text=current_card["French"], fill="black")
        canvas.itemconfig(lang_Name, text="French", fill="black")
        canvas.itemconfig(card_front, image=small_front_Image)
        flip_timer = window.after(3000, func=flip_Card)
    else:
        canvas.itemconfig(word, text="Koniec nauki!", fill="black")
        canvas.itemconfig(lang_Name, text="", fill="black")
        window.after_cancel(flip_timer)


def flip_Card():
    canvas.itemconfig(lang_Name, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_front, image=card_back)


def is_known():
    global fr_Words
    fr_Words = [word for word in fr_Words if word != current_card]
    print(len(fr_Words))
    pandas.DataFrame(fr_Words).to_csv("data/words_to_learn.csv", index=False)

    if len(fr_Words) == 0:
        show_message()
    else:
        next_Card()

def show_message():
    messagebox.showinfo(title="Gratulacje!", message="Ukończyłeś naukę wszystkich słów!")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_Card)

# Canvas
canvas = tk.Canvas(width=500, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Front Card Image
front_Image = PhotoImage(file="images/card_front.png")
small_front_Image = front_Image.subsample(2, 2)
card_front = canvas.create_image(250, 200, image=small_front_Image)

# Back Card Image
back_Image = PhotoImage(file="images/card_back.png")
small_back_Image = back_Image.subsample(2, 2)
card_back = small_back_Image

# text
lang_Name = canvas.create_text(250, 120, text=name, font=("Ariel", 20, "italic"))

word = canvas.create_text(250, 200, text="Language", font=("Ariel", 20, "bold"))

# Button
cross_image = PhotoImage(file="images/wrong.png")
unknow_button = Button(image=cross_image, highlightthickness=0)
unknow_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0)
know_button.grid(column=1, row=1)

# when the button is clicked
know_button.config(command=is_known)
unknow_button.config(command=next_Card)

next_Card()

window.mainloop()
