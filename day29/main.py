import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(0, nr_letters)]
    password_list += [random.choice(symbols) for _ in range(0, nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(0, nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except json.JSONDecodeError:
            data = {}

        # Updating old data with new data
        data.update(new_data)

        # Saving updated data
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)  # Save the entire 'data' dictionary, not just 'new_data'

        reset_info()


def reset_info():
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    website_entry.focus()


# ----------------------------- FIND PASSWORD -------------------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    finally:
        reset_info()


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.config(width=33)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.config(width=52)
email_entry.insert(0, "@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)
password_entry.config(width=33)

# Buttons
generate_pass_butt = tk.Button(text="Generate Password", command=generate_password)
generate_pass_butt.grid(column=2, row=3)

add_butt = tk.Button(text="Add", width=36)
add_butt.grid(column=1, row=4, columnspan=2)
add_butt.config(width=44)

add_butt.config(command=get_info)

add_Search = tk.Button(text="Search", width=14, command=find_password)
add_Search.grid(column=2, row=1)

window.mainloop()
