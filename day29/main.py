import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n "
                                                              f"Password: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                reset_info()


def reset_info():
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    website_entry.focus()


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
website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.config(width=52)
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

window.mainloop()
