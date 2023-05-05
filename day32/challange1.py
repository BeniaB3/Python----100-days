import smtplib
import random
import datetime as dt

MY_EMAIL = "youremail@gmail.com"
PASSWORD = "yurpaswword"


with open("quotes.txt") as file:
    allText = file.readlines()


def randomText():
    return random.choice(allText)


def sendEmail(mail_send):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=mail_send,
                            msg=f"Subject:Motivational quote\n\n{randomText()}")


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    sendEmail("theiremail@yahoo.com")