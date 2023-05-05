import smtplib

# put your email
my_email = "youremail@gmail.com"
# Password from gmail app password
password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="theiremail@yahoo.com", # where you want send
                        msg="Subject:Hello\n\nThis is the body of my email")
