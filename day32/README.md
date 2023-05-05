 # Birthday Emailer README.md

 ## Description

This Python script sends out personalized birthday emails to a list of recipients in a CSV file. It picks a random pre-written birthday message, inserts the recipient's name, and sends the email using the Gmail SMTP server.

 ## Requirements

 - Python 3.6 or higher
 - A Gmail account with "Less Secure Apps" enabled

 ## Files

 - main.py: The main script for the birthday emailer
 - birthdays.csv: The CSV file containing names, email addresses, and birth dates
 - texts: A folder containing the pre-written birthday messages
 - letter_1.txt: Birthday message template 1
 - letter_2.txt: Birthday message template 2
 - letter_3.txt: Birthday message template 3

 ## Setup

 1. Replace youremail.com and yourpassword with your Gmail email address and password in the MY_EMAIL and PASSWORD variables.
 2. Update the birthdays.csv file with the names, email addresses, and birth dates of the recipients.
 3. Customize the birthday message templates (letter_1.txt, letter_2.txt, letter_3.txt) as needed. Make sure to include [NAME] as a placeholder for the recipient's name.

 ## Usage

 Run the script using Python:

 // python main.py //

 The script will automatically send out personalized birthday emails to recipients whose birthdays are on the current date.

 ## Note

 Make sure to enable "Less Secure Apps" in your Gmail account settings for this script to work. Be aware that enabling this setting may pose a security risk to your account. It's recommended to create a separate Gmail account for this purpose.