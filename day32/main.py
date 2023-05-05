import random
import datetime as dt
import smtplib

MY_EMAIL = "youremail.com"
PASSWORD = "yourpassword"


def randomLetter(name):
    with open(f"./texts/letter_{random.randint(1, 3)}.txt") as file:
        text = file.read()
        text = text.replace("[NAME]", name)
        return text


def textToSend():
    birthdayList = []
    with open("birthdays.csv") as file:
        data = file.readlines()
        for line in data[1:]:
            line = line.strip()
            if not line or len(line.split(",")) != 5:
                continue
            name, email, birth_year, birth_month, birth_day = line.split(",")
            if int(birth_month) == month and int(birth_day) == day:
                letter = randomLetter(name)
                birthdayList.append((letter, email))
    return birthdayList


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    for text, email in textToSend():
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject:Happy birthday!\n\n{text}")
