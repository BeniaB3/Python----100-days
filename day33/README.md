

## This Python script tracks the International Space Station (ISS) and sends an email notification when it is above your location and it is dark outside.

### Main dependencies:
 - requests
 - smtplib
 - datetime

### How it works:
 1. Get the current ISS position using the Open Notify API (http://api.open-notify.org/iss-now.json)
 2. Get sunrise and sunset times for your location using the Sunrise Sunset API (https://api.sunrise-sunset.org/json)
 3. Check if the ISS is close to your location by comparing its latitude and longitude with your predefined latitude and longitude (MY_LAT and MY_LONG).
 4. Check if it is dark outside by comparing the current time with the sunrise and sunset times.
 5. If the ISS is close and it is dark outside, send an email notification using Gmail's SMTP server (smtp.gmail.com).
 6. The script will keep running and checking the ISS position every 180 seconds (3 minutes).

### To use the script, replace the following variables with your own information:
 - MY_LAT: Your latitude
 - MY_LONG: Your longitude
 - MY_EMAIL: Your Gmail email address
 - MY_PASSWORD: Your Gmail password
 - Email recipient address (in the send_email() function)

Note: It is not recommended to store your email credentials in the script. Consider using environment variables or other secure methods to store sensitive information.

