import smtplib
import datetime as dt
import random

# Constants
MY_EMAIL = "YOUR_MAIL"
PASSWORD = "YOUR_PASSWORD"


# Sending email
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Opening quotes.txt
    with open("quotes.txt", "r") as data:
        file_data = data.readlines()
        random_quote = random.choice(file_data)

    # Getting the day of the week from datetime module
    now = dt.datetime.now()
    weekday = now.weekday()

    # Checking if it is Friday
    if weekday == 4:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Motivation quote\n\n {random_quote}")

