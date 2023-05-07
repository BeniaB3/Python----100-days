import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.229675  # Your latitude
MY_LONG = 21.012230  # Your longitude

MY_EMAIL = "yourmail1@gmail.com"
MY_PASSWORD = "yourpassword"


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


def get_sunrise_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset


def is_iss_close(iss_latitude, iss_longitude):
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


def is_dark(sunrise, sunset, time_now):
    return time_now.hour >= sunset or time_now.hour <= sunrise


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="yourmail2@yahoo.com",
                            msg="Subject: Look Up!\n\nThe ISS is above you in the sky.")
        print("Email sent")


def main():
    iss_latitude, iss_longitude = get_iss_position()
    sunrise, sunset = get_sunrise_sunset()
    time_now = datetime.now()
    while True:
        time.sleep(180)
        if is_iss_close(iss_latitude, iss_longitude):
            if is_dark(sunrise, sunset, time_now):
                send_email()
            else:
                print("It's daytime")
        else:
            print("The ISS is not close to your position")


if __name__ == "__main__":
    main()
