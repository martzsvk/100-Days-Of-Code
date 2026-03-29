##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import random
import datetime as dt

# Constants
MY_EMAIL = "YOUR_MAIL"
PASSWORD = "YOUR_PASSWORD"


# Sending an email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    # Opening birthdays.csv
    data = pandas.read_csv("birthdays.csv")
    # Creating list for letters
    letters_list = ["./letter_templates/letter_1.txt",
                    "./letter_templates/letter_2.txt",
                    "./letter_templates/letter_3.txt"]
    # Opening random letter
    with open(f"{random.choice(letters_list)}", "r") as letter:
        letter_data = letter.read()

        # Getting the month and the day
        now = dt.datetime.now()
        month = now.month
        day = now.day

        # Iterating through rows
        for row in data.itertuples():
            if row.month == month and row.day == day:
                # Replacing [NAME] with the row name
                replaced_data = letter_data.replace("[NAME]", f"{row.name}")
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=data.email, msg=f"Subject: Happy birthday \n\n {replaced_data}")





